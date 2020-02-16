use clipboard::ClipboardContext;
use clipboard::ClipboardProvider;
use colored::*;

use crate::error::BoxResult;
use clap::ArgMatches;
use std::process::exit;

pub fn handle_result(output: &str, matches: &ArgMatches) -> () {
    if matches.is_present("clip") {
        let mut ctx: ClipboardContext = ClipboardProvider::new().unwrap();
        ctx.set_contents(output.to_owned()).unwrap();
        if !matches.is_present("suppress") {
            print!("{}", output.yellow());
            print!("{}", " (📋 Copied to clipboard.)\n".green())
        }
    } else {
        if !matches.is_present("suppress") {
            println!("{}", output)
        }
    }
}

pub fn handle_error(message: &str) {
    println!("{}{}", "ERROR: ".red(), message.red());
    exit(1);
}
