#[macro_use]
extern crate clap;

use clap::App;

mod util;
mod uuid;
mod version;

fn main() {
    // The YAML file is found relative to the current file, similar to how modules are found
    let yaml = load_yaml!("cli.yaml");
    let matches = &App::from_yaml(yaml).get_matches();
    let subcommand_options = matches.subcommand().1.unwrap();

    let subcommand = match matches.subcommand_name() {
        Some("uuid") => uuid::generate_uuid,
        Some("version") => version::show_version,
        _ => unreachable!(),
    };
    util::clip_result(subcommand_options)(subcommand);
}
