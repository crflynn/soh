use clap::ArgMatches;

use crate::error::BoxResult;
use base64;
use clipboard::{ClipboardContext, ClipboardProvider};
use std::str;

pub fn b64(matches: &ArgMatches) -> BoxResult<String> {
    let input = {
        if let Some(v) = matches.subcommand().1.unwrap().value_of("INPUT") {
            v.to_string()
        } else {
            println!("No argument passed. Using clipboard contents...");
            let mut ctx: ClipboardContext = ClipboardProvider::new().unwrap();
            ctx.get_contents().unwrap()
        }
    };
    match matches.subcommand_name() {
        Some("e") => Ok(base64::encode(&input)),
        Some("d") => {
            let decoded = base64::decode(&input).unwrap();
            Ok(String::from(str::from_utf8(&decoded)?))
        }
        _ => unreachable!(),
    }
}
