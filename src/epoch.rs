use crate::error::BoxResult;
use clap::ArgMatches;
use std::time::SystemTime;

pub fn epoch(matches: &ArgMatches) -> BoxResult<String> {
    let now = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .expect("Error fetching system time");
    match matches.subcommand_name() {
        Some("s") => Ok(now.as_secs().to_string()),
        Some("m") => Ok(now.as_millis().to_string()),
        Some("u") => Ok(now.as_micros().to_string()),
        Some("n") => Ok(now.as_nanos().to_string()),
        _ => unreachable!(),
    }
}
