use crate::error::BoxResult;
use clap::ArgMatches;
use reqwest;
use std::net::ToSocketAddrs;
use sys_info;

pub fn sys(matches: &ArgMatches) -> BoxResult<String> {
    match matches.subcommand_name() {
//        Some("arch") => Ok(num_cpus::get().to_string()),  // conditional compile?
        Some("cores") => Ok(sys_info::cpu_num()?.to_string()),
        Some("eip") => Ok(reqwest::blocking::get("https://api.ipify.org/")?.text()?),
        Some("ip") => {
            let mut host = sys_info::hostname()?;
            host.push_str(":443");
            let mut addrs_iter = host.to_socket_addrs().unwrap();
            let address = addrs_iter.next().unwrap().to_string();
            let addr: Vec<&str> = address.split(":443").collect();
            Ok(addr[0].to_string())
        }
        Some("mac") => Ok(mac_address::get_mac_address().unwrap().unwrap().to_string()),
        Some("node") => Ok(sys_info::hostname()?),
        Some("os") => Ok(sys_info::os_type()?),
        //        Some("proc") => Ok(cpuid::identify().unwrap().codename),  // cpuid wont compile
        Some("osver") => Ok(sys_info::os_release()?),
        _ => unreachable!(),
    }
}
