use crate::error::BoxResult;
use chrono::{NaiveDateTime, TimeZone};
use chrono::{SecondsFormat, Utc};
use chrono_tz::Tz;
use clap::ArgMatches;
use std::convert::TryFrom;

pub fn datetime(matches: &ArgMatches) -> BoxResult<String> {
    let subcommand_matches = matches
        .subcommand_matches(matches.subcommand_name().unwrap())
        .unwrap();

    let timezone = subcommand_matches.value_of("timezone").unwrap_or("UTC");
    let tz = match timezone.parse::<Tz>() {
        Ok(v) => v,
        Err(e) => return Err(Box::try_from(e).unwrap()),
    };

    let seconds_format = subcommand_matches.value_of("seconds").unwrap_or("m");
    let sf = match seconds_format {
        "s" => SecondsFormat::Secs,
        "m" => SecondsFormat::Millis,
        "u" => SecondsFormat::Micros,
        "n" => SecondsFormat::Nanos,
        _ => return Err(Box::try_from("Seconds format must be one of (s, m, u, n)").unwrap()),
    };

    let now = match subcommand_matches.value_of("epoch") {
        Some(e) => {
            let epoch: f64 = match e.parse::<f64>() {
                Ok(s) => s,
                Err(e) => return Err(Box::try_from(e).unwrap()),
            };
            let seconds = epoch as i64;
            let ns = ((epoch - seconds as f64) * 1_000_000_000.0) as u32;
            println!("{:?}", epoch);
            println!("{:?}", epoch - seconds as f64);
            let naive_datetime = NaiveDateTime::from_timestamp(seconds, ns);
            tz.from_utc_datetime(&naive_datetime)
        }
        _ => tz.from_utc_datetime(&Utc::now().naive_utc()),
    };

    let result = match matches.subcommand_name() {
        Some("now") => now.to_string(),
        Some("ts") => now.to_rfc3339_opts(sf, true),
        Some("date") => now.date().to_string(),
        Some("time") => now.time().to_string(),
        _ => unreachable!(),
    };

    Ok(result.to_string())
}
