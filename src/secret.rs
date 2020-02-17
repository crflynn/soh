use crate::error::BoxResult;
use clap::ArgMatches;
use rand::seq::SliceRandom;
use rand::thread_rng;
use std::convert::TryFrom;

const LETTERS: &str = "abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
const NUMBERS: &str = "1234567890";
const SYMBOLS: &str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
const HEX: &str = "1234567890abcdef";
const URLSAFE: &str = "1234567890abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._~()'!*:@,;";

pub fn secret(matches: &ArgMatches) -> BoxResult<String> {
    let subcommand_matches = matches
        .subcommand_matches(matches.subcommand_name().unwrap())
        .unwrap();

    let length = subcommand_matches.value_of("length");
    let l: i32 = match length {
        Some(v) => match v.parse() {
            Ok(v) => v,
            _ => return Err(Box::try_from("Secret length must be an integer").unwrap()),
        },
        _ => 32,
    };

    match matches.subcommand_name() {
        Some("pw") => pw(l, subcommand_matches),
        Some("h") => hex(l),
        Some("u") => urlsafe(l),
        _ => unreachable!(),
    }
}

pub fn hex(l: i32) -> BoxResult<String> {
    let hex = HEX.as_bytes();
    let mut key = Vec::with_capacity(l as usize);

    let mut rng = thread_rng();
    for _ in 0..l {
        key.push(*hex.choose(&mut rng).unwrap() as u8)
    }
    Ok(String::from_utf8(key).unwrap())
}

pub fn urlsafe(l: i32) -> BoxResult<String> {
    let url = URLSAFE.as_bytes();
    let mut key = Vec::with_capacity(l as usize);

    let mut rng = thread_rng();
    for _ in 0..l {
        key.push(*url.choose(&mut rng).unwrap() as u8)
    }
    Ok(String::from_utf8(key).unwrap())
}

pub fn pw(l: i32, matches: &ArgMatches) -> BoxResult<String> {
    let numbers = matches.value_of("numbers");
    let symbols = matches.value_of("symbols");

    let n: i32 = match numbers {
        Some(v) => match v.parse() {
            Ok(v) => v,
            _ => return Err(Box::try_from("Number quantity must be an integer").unwrap()),
        },
        _ => 8,
    };
    let s: i32 = match symbols {
        Some(v) => match v.parse() {
            Ok(v) => v,
            _ => return Err(Box::try_from("Symbol quantity must be an integer").unwrap()),
        },
        _ => 4,
    };

    if (n + s > l) | (n < 0) | (s < 0) | (l < 0) {
        return Err(Box::from(
            "Password length must exceed character requirements".to_string(),
        ));
    }

    let allowed_characters = if matches.is_present("ambiguous") {
        LETTERS.to_string()
    } else {
        LETTERS.replace(&['I', 'i', 'l', '1', 'L', 'o', '0', 'O'][..], "")
    }
    .to_string()
    .into_bytes();

    let mut rng = thread_rng();

    let mut chars: Vec<u8> = Vec::with_capacity(l as usize);
    for _ in 0..(l - n - s) {
        chars.push(*allowed_characters.choose(&mut rng).unwrap() as u8)
    }
    let nums = NUMBERS.as_bytes();
    for _ in 0..n {
        chars.push(*nums.choose(&mut rng).unwrap() as u8)
    }
    let syms = SYMBOLS.as_bytes();
    for _ in 0..s {
        chars.push(*syms.choose(&mut rng).unwrap() as u8)
    }

    chars.shuffle(&mut rng);

    Ok(String::from_utf8(chars).unwrap())
}
