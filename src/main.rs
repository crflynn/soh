#[macro_use]
extern crate clap;

use clap::App;

mod b64;
mod epoch;
mod error;
mod sys;
mod util;
mod uuid;
mod version;

fn main() {
    // The YAML file is found relative to the current file, similar to how modules are found
    let yaml = load_yaml!("cli.yaml");
    let matches = &App::from_yaml(yaml).get_matches();

    let subcommand = match matches.subcommand_name() {
        Some("b64") => b64::b64,
        Some("epoch") => epoch::epoch,
        Some("sys") => sys::sys,
        Some("uuid") => uuid::generate_uuid,
        Some("version") => version::show_version,
        _ => unreachable!(),
    };
    util::handle_result(matches)(subcommand);
}
