use std::io::{Read, Write};
use std::net::TcpStream;
use std::time;

// DELAYS (ms)
const ONE: u128 = 100;
const ZERO: u128 = 25;

fn main() {
    //let ip = "127.0.0.1:1337"; // my local server
    let ip = "138.47.165.156:31337"; // timo's server
    let mut timings = Vec::new();
    if let Ok(mut stream) = TcpStream::connect(ip) {
        let mut stdout = std::io::stdout().lock();
        let mut data = [0; 32];
        loop {
            match stream.read(&mut data) {
                Ok(0) => break,
                Ok(bytes) => {
                    timings.push(time::Instant::now());
                    // print incoming unless it's EOF
                    if data[0..bytes] != [b'E', b'O', b'F'] {
                        stdout.write(&data[0..bytes]).unwrap();
                        stdout.flush().unwrap();
                    }
                }
                Err(err) => {
                    println!("{}", err);
                }
            }
        }
        stdout.write(&[b'\n']).unwrap(); // print newline
    } else {
        panic!("failed to connect to server");
    }

    // split on the average between ONE and ZERO
    // This tended to produce more consistent results in our testing
    let split = (ONE + ZERO) / 2;

    let mut hidden_msg = timings
        .windows(2)
        .map(|x| x[1].duration_since(x[0]).as_millis())
        .collect::<Vec<u128>>()
        .iter()
        .map(mapper(ONE, ZERO, split))
        .collect::<String>()
        .as_bytes()
        .chunks(8)
        .map(|x| std::str::from_utf8(x).unwrap())
        .map(|x| format!("{:0>8}", x))
        .map(|x| u8::from_str_radix(&x, 2).unwrap())
        .map(|x| x as char)
        .collect::<String>();

    if hidden_msg.contains("EOF") {
        hidden_msg = hidden_msg.replace("EOF", "");
    }

    println!("{}", hidden_msg);
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
