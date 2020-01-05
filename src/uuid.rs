use clap::ArgMatches;
use std::time::SystemTime;
use uuid::v1::Context;
use uuid::v1::Timestamp;
use uuid::Uuid;

pub fn generate_uuid(matches: &ArgMatches) -> Result<String, String> {
    let version = matches.value_of("version");

    let namespace = matches.value_of("namespace");
    let name = matches.value_of("name").unwrap_or("");

    let uuid = match version {
        Some("1") => generate_v1(),
        Some("3") => generate_v3(namespace, name),
        Some("4") => generate_v4(),
        Some("5") => generate_v5(namespace, name),
        None => generate_v4(),
        _ => Err("UUID version must be 1, 3, 4, or 5".to_string()),
    }?;
    if matches.is_present("upper") {
        return Ok(uuid.to_uppercase());
    }
    Ok(uuid)
}

fn generate_v1() -> Result<String, String> {
    let mac = mac_address::get_mac_address().unwrap().unwrap();
    let context = Context::new(42);
    let now = SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .expect("Error fetching system time");
    let ts = Timestamp::from_unix(&context, now.as_secs(), now.subsec_nanos());
    let uuid = Uuid::new_v1(ts, &mac.bytes()).expect("failed to generate UUID");
    Ok(uuid.to_string())
}

fn generate_v3(namespace: Option<(&str)>, name: &str) -> Result<String, String> {
    let ns = get_namespace(namespace)?;
    let uuid = Uuid::new_v3(&ns, name.as_bytes());
    Ok(uuid.to_string())
}

fn generate_v4() -> Result<String, String> {
    Ok(Uuid::new_v4().to_string())
}

fn generate_v5(namespace: Option<(&str)>, name: &str) -> Result<String, String> {
    let ns = get_namespace(namespace)?;
    let uuid = Uuid::new_v3(&ns, name.as_bytes());
    Ok(uuid.to_string())
}

fn get_namespace(namespace: Option<(&str)>) -> Result<Uuid, String> {
    match namespace {
        Some("dns") => Ok(Uuid::NAMESPACE_DNS),
        Some("oid") => Ok(Uuid::NAMESPACE_OID),
        Some("url") => Ok(Uuid::NAMESPACE_URL),
        Some("x500") => Ok(Uuid::NAMESPACE_X500),
        _ => Err("Invalid namespace, must be in {dns, oid, url, x500}".to_string()),
    }
}
