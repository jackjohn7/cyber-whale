use std::io::{Read, Write};
use std::net::TcpStream;
use std::time;

const ONE: u128 = 100;
const ZERO: u128 = 25;

fn main() {
    let ip = "127.0.0.1:1337";
    // let ip = "138.47.165.156:31337"; // timo's server
    let mut timings = Vec::new();
    if let Ok(mut stream) = TcpStream::connect(ip) {
        let mut stdout = std::io::stdout().lock();
        loop {
            let mut data = [0; 4096];
            match stream.read(&mut data[0..100]) {
                Ok(0) => break,
                Ok(bytes) => {
                    timings.push(time::Instant::now());
                    stdout.write(&data[0..bytes]).unwrap();
                    stdout.flush().unwrap();
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

    let one = ONE - 5;
    let zero = ZERO - 5;

    let mut hidden_msg = timings
        .windows(2)
        .map(|x| x[1].duration_since(x[0]).as_millis())
        .collect::<Vec<u128>>()
        .iter()
        .map(mapper(one, zero))
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

    // The logic separated into pieces
    //  This is just useful for debugging

    //let diffs = timings
    //    .windows(2)
    //    .map(|x| (x[0], x[1]))
    //    .map(|(a, b)| b.duration_since(a))
    //    .map(|d| d.as_millis())
    //    .collect::<Vec<u128>>();
    //let binary = diffs.iter().map(mapper(one, zero)).collect::<String>();
    //let r = binary
    //    .as_bytes()
    //    .chunks(8)
    //    .map(|x| std::str::from_utf8(x).unwrap())
    //    .map(|x| format!("{:0>8}", x))
    //    .map(|x| u8::from_str_radix(&x, 2).unwrap())
    //    .map(|x| x as char)
    //    .collect::<String>();
    //dbg!(r);
}

/// Creates mapping closure given a one and zero value
fn mapper(one: u128, zero: u128) -> impl for<'a> Fn(&'a u128) -> char {
    return move |x: &u128| {
        if one > 0 {
            if x.clone() > one as u128 {
                '1'
            } else {
                '0'
            }
        } else {
            if x.clone() > zero {
                '0'
            } else {
                '1'
            }
        }
    };
}
