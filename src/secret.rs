use crate::error::BoxResult;
use clap::ArgMatches;
use std::convert::TryFrom;
use rand::thread_rng;
use rand::seq::SliceRandom;


const LETTERS: &str = "abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const NUMBERS: &str = "1234567890";
const SYMBOLS: &str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";


pub fn secret(matches: &ArgMatches) -> BoxResult<String> {
    match matches.subcommand_name() {
        Some("pw") => pw(matches
            .subcommand_matches(matches.subcommand_name().unwrap())
            .unwrap()),
        _ => unreachable!(),
    }
}

pub fn pw(matches: &ArgMatches) -> BoxResult<String> {
    let numbers = matches.value_of("numbers");
    let symbols = matches.value_of("symbols");
    let length = matches.value_of("length");

    let l: i32 = match length {
        Some(v) => match v.parse() {
            Ok(v) => v,
            _ => return Err(Box::try_from("Password length must be an integer").unwrap())
        },
        _ => 32,
    };
    let n: i32 = match numbers {
        Some(v) => match v.parse() {
            Ok(v) => v,
            _ => return Err(Box::try_from("Number quantity must be an integer").unwrap())
        },
        _ => 8,
    };
    let s: i32 = match symbols {
        Some(v) => match v.parse() {
            Ok(v) => v,
            _ => return Err(Box::try_from("Symbol quantity must be an integer").unwrap())
        },
        _ => 4,
    };

    if (n + s > l) | (n < 0) | (s < 0) | (l < 0) {
        return Err(Box::from(
            "Password length must exceed character requirements".to_string(),
        ));
    }

    let allowed_characters = match matches.is_present("ambiguous") {
        false => {
            LETTERS.replace(&['I','i','l','1','L','o','0','O'][..], "")
        },
        true => LETTERS.to_string(),
    }.to_string().into_bytes();

    let mut rng = thread_rng();

    let mut chars:Vec<u8> = vec![];
    for _ in 0..(l-n-s) {
        chars.push(*allowed_characters.choose(&mut rng).unwrap())
    }
    let nums = NUMBERS.as_bytes();
    for _ in 0..n {
        chars.push(*nums.choose(&mut rng).unwrap())
    }
    let syms = SYMBOLS.as_bytes();
    for _ in 0..s {
        chars.push(*syms.choose(&mut rng).unwrap())
    }

    chars.shuffle(&mut rng);

    Ok(String::from_utf8(chars).unwrap())
}
