use clipboard::ClipboardContext;
use clipboard::ClipboardProvider;
use colored::*;

use clap::ArgMatches;
use std::process::exit;

pub fn clip_result<'a>(
    matches: &'a ArgMatches,
) -> impl Fn(fn(m: &'a ArgMatches) -> Result<String, String>) -> () + 'a {
    let get_result = move |subcommand: fn(m: &'a ArgMatches) -> Result<String, String>| -> () {
        let result = subcommand(matches);

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
