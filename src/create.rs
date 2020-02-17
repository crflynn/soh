use crate::error::BoxResult;
use clap::ArgMatches;
use std::convert::TryFrom;
use std::collections::BTreeMap;
use reqwest;
use serde::{Deserialize, Serialize};
use reqwest::header::USER_AGENT;
use std::fs::File;
use std::io::Write;
use std::path::Path;

const GITIGNORE_FILE: &str = ".gitignore";
const GITIGNORE_URL: &str = "https://api.github.com/repos/github/gitignore/contents";
const LICENSE_FILE: &str = "LICENSE.txt";
const LICENSE_URL: &str = "https://api.github.com/repos/github/choosealicense.com/contents/_licenses";
const SOH_USER_AGENT: &str = "soh/0.2.0";

// deserialize JSON responses into this struct
// download_url will be null for folder objects
#[derive(Debug, Serialize, Deserialize)]
struct GithubContentsEntry {
    name: String,
    download_url: Option<String>,
}

pub fn create(matches: &ArgMatches) -> BoxResult<String> {
    let subcommand_matches = matches
        .subcommand_matches(matches.subcommand_name().unwrap())
        .unwrap();

    match matches.subcommand_name() {
        Some("gitignore") => github_download(subcommand_matches, GITIGNORE_FILE, GITIGNORE_URL),
        Some("license") => github_download(subcommand_matches, LICENSE_FILE, LICENSE_URL),
        _ => unreachable!(),
    }
}

pub fn github_download(matches: &ArgMatches, filename: &str, url: &str) -> BoxResult<String> {
    let overwrite = matches.is_present("overwrite");
    let object_type = matches.value_of("INPUT").unwrap();

    if object_type != "list" && !overwrite && Path::new(filename).exists() {
        return Err(Box::try_from("File already exists; aborting. Use -o to overwrite file.").unwrap())
    }

    let client = reqwest::blocking::Client::new();
    let result = client.get(url).header(USER_AGENT, SOH_USER_AGENT).send();

    let response: Vec<GithubContentsEntry> = result.unwrap().json::<Vec<GithubContentsEntry>>().unwrap();

    // use a btree to maintain the order
    let mut files: BTreeMap<String, String> = BTreeMap::new();

    // pack lower-case names, file download urls into map
    for entry in response.iter() {
        let l: Vec<&str> = entry.name.split('.').collect();
        if l.len() > 1 && l[0] != ""{
            files.insert(l[0].to_lowercase(), entry.download_url.as_ref().unwrap().to_string());
        }
    }

    let lower_name = object_type.to_lowercase();
    match lower_name.as_str() {
        "list" =>  {
            let keys: Vec<String> = files.keys().cloned().collect();
            Ok(keys.join("\n"))
        }
        v => {
            // ensure that the entity of interest is in the list of entities
            let download_url = match files.get(v){
                Some(v) => v,
                None => return Err(Box::try_from("Must supply a valid value. Run with `list` to see valid values").unwrap())
            };
            let file_response = client.get(download_url).header(USER_AGENT, SOH_USER_AGENT).send();
            let mut contents: String = file_response.unwrap().text().unwrap();
            // license files have additional frontmatter that needs to be stripped away
            if filename == LICENSE_FILE {
                let components: Vec<&str> = contents.split("\n---\n").collect();
                contents = components.last().unwrap().trim().to_string()
            }
            let mut file_response = File::create(filename)?;
            write!(file_response, "{}", contents)?;
            Ok(format!("File {} was created.", filename))
        }
    }
}