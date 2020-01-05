use std::error;

pub type BoxResult<T> = std::result::Result<T, Box<dyn error::Error>>;
