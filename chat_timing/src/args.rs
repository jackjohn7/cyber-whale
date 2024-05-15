use clap::Parser;

#[derive(Parser, Debug)]
#[command(
    version,
    about = "Tool used to uncover hidden messages encoded within delays over TCP servers",
    long_about = "Tool used to uncover hidden messages encoded within delays over TCP servers. Written in Rust."
)]
pub struct Args {
    #[arg(long, default_value = "127.0.0.1")]
    pub ip: String,
    #[arg(short, long, default_value = "1337")]
    pub port: String,
    #[arg(short, long, default_value_t = 100)]
    pub one: u128,
    #[arg(short, long, default_value_t = 25)]
    pub zero: u128,
    #[clap(long, short, action)]
    pub debug: bool,
}
