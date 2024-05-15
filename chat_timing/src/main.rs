use clap::Parser;
use std::io::{Read, Write};
use std::net::TcpStream;
use std::time;

pub mod args;

/// Provided an IP, collect the raw timings from the server
fn get_data(ip: String) -> Result<Vec<time::Instant>, String> {
    let mut timings = Vec::new();
    if let Ok(mut stream) = TcpStream::connect(ip) {
        let mut stdout = std::io::stdout().lock();
        stdout
            .write(b"Reading: ")
            .map_err(|err| format!("Error: {}", err))?;
        let mut data = [0; 32];
        loop {
            match stream.read(&mut data) {
                Ok(0) => break,
                Ok(bytes) => {
                    timings.push(time::Instant::now());
                    // print incoming unless it's EOF
                    if data[0..bytes] != [b'E', b'O', b'F'] {
                        stdout
                            .write(&data[0..bytes])
                            .map_err(|err| format!("Error: {}", err))?;
                        stdout.flush().map_err(|err| format!("Error: {}", err))?;
                    }
                }
                Err(err) => {
                    println!("{}", err);
                }
            }
        }
        stdout
            .write(&[b'\n'])
            .map_err(|err| format!("Error: {}", err))?; // print newline
        Ok(timings) // return timings
    } else {
        Err(String::from("failed to connect to server"))
    }
}

/// Provided timings, ONE, and ZERO split values, parse message
fn get_msg(timings: Vec<time::Instant>, one: u128, zero: u128) -> Result<String, String> {
    // split on the average between ONE and ZERO
    // This tended to produce more consistent results in our testing
    let split = (one + zero) / 2;

    let mut hidden_msg = timings
        .windows(2)
        .map(|x| x[1].duration_since(x[0]).as_millis())
        .collect::<Vec<u128>>()
        .iter()
        .map(mapper(one, zero, split))
        .collect::<String>()
        .as_bytes()
        .chunks(8)
        .map(|x| std::str::from_utf8(x).map_err(|err| format!("Error: {}", err)))
        .collect::<Result<Vec<&str>, _>>()?
        .iter()
        .map(|x| format!("{:0>8}", x))
        .map(|x| u8::from_str_radix(&x, 2).map_err(|err| format!("Error: {}", err)))
        .collect::<Result<Vec<u8>, _>>()?
        .iter()
        .map(|x| *x as char)
        .collect::<String>();

    if hidden_msg.contains("EOF") {
        hidden_msg = hidden_msg.replace("EOF", "");
    }

    Ok(hidden_msg)
}

fn main() -> Result<(), String> {
    let args = args::Args::parse();
    if args.debug {
        dbg!(&args);
    }

    let addr = format!("{}:{}", args.ip, args.port);
    let timings = get_data(addr)?;
    let hidden_msg = get_msg(timings, args.one, args.zero)?;

    println!("{}", hidden_msg);

    Ok(())
}

/// Creates mapping closure given a one and zero value
fn mapper(one: u128, zero: u128, split: u128) -> impl for<'a> Fn(&'a u128) -> char {
    return move |x: &u128| {
        if one > zero {
            if x.clone() > split {
                '1'
            } else {
                '0'
            }
        } else {
            if x.clone() > split {
                '0'
            } else {
                '1'
            }
        }
    };
}
