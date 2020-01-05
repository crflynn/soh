use clap::ArgMatches;

pub const VERSION: &str = "0.2.0";

pub fn show_version(_matches: &ArgMatches) -> Result<String, String> {
    let result = VERSION.to_string();
    Ok(result)
}
