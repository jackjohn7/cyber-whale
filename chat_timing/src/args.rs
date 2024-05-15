use clap::Parser;

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
pub struct Args {
    #[arg(short, long, default_value = "127.0.0.1")]
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
