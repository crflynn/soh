#[macro_use]
extern crate clap;

use clap::App;

mod b64;
mod error;
mod util;
mod uuid;
mod version;

fn main() {
    // The YAML file is found relative to the current file, similar to how modules are found
    let yaml = load_yaml!("cli.yaml");
    let matches = &App::from_yaml(yaml).get_matches();

    let subcommand = match matches.subcommand_name() {
        Some("uuid") => uuid::generate_uuid,
        Some("version") => version::show_version,
        Some("b64") => b64::b64,
        _ => unreachable!(),
    };
    util::clip_result(matches)(subcommand);
}
