use clipboard::ClipboardContext;
use clipboard::ClipboardProvider;
use colored::*;

use crate::error::BoxResult;
use clap::ArgMatches;
use std::process::exit;

pub fn handle_result<'a>(
    matches: &'a ArgMatches,
) -> impl Fn(fn(m: &'a ArgMatches) -> BoxResult<String>) -> () + 'a {
    let get_result = move |subcommand: fn(m: &'a ArgMatches) -> BoxResult<String>| -> () {
        let subcommand_options = matches.subcommand().1.unwrap();
        let result = subcommand(subcommand_options);

        let output = match result {
            Err(msg) => {
                println!("ERROR: {}", msg);
                exit(1);
            }
            Ok(value) => value,
        };

        if matches.is_present("clip") {
            let mut ctx: ClipboardContext = ClipboardProvider::new().unwrap();
            ctx.set_contents(output.to_owned()).unwrap();
            print!("{}", output.yellow());
            print!("{}", " (📋 Copied to clipboard.)\n".green())
        } else {
            println!("{}", output)
        }
    };

    return get_result;
}
