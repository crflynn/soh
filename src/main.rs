#[macro_use]
extern crate clap;

use clap::App;

mod b64;
mod create;
mod datetime;
mod epoch;
mod error;
mod output;
mod secret;
mod sys;
mod uuid;
mod version;

fn main() {
    let yaml = load_yaml!("cli.yaml");
    let matches = &App::from_yaml(yaml).get_matches();

    let subcommand = match matches.subcommand_name() {
        Some("b64") => b64::b64,
        Some("create") => create::create,
        Some("dt") => datetime::datetime,
        Some("epoch") => epoch::epoch,
        Some("secret") => secret::secret,
        Some("sys") => sys::sys,
        Some("uuid") => uuid::generate_uuid,
        Some("version") => version::show_version,
        _ => unreachable!(),
    };

    let subcommand_matches = matches
        .subcommand_matches(matches.subcommand_name().unwrap())
        .unwrap();

    match subcommand(subcommand_matches) {
        Ok(message) => output::handle_result(message.as_str(), &matches),
        Err(message) => output::handle_error(&message.to_string()),
    };
}
