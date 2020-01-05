use crate::error::BoxResult;
use clap::ArgMatches;

pub const VERSION: &str = "0.2.0";

pub fn show_version(_matches: &ArgMatches) -> BoxResult<String> {
    let result = VERSION.to_string();
    Ok(result)
}
