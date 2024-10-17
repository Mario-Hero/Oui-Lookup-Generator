use std::collections::HashMap;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    //***insert_point***
    const oui_data:HashMap<u32, &'static str> = HashMap::from(
        [(1, "hello")]
    );
    //***insert_point***
    for mac in args.iter().skip(1) {
        let mut mac_digit: u32 = 0;
        let mut add_times: u32 = 0;
        for c in mac.chars() {
            if c.is_alphanumeric() {
                mac_digit = mac_digit * 16 + c.to_digit(16).unwrap_or(0);
                add_times += 1;
                if add_times >= 6 {
                    break;
                }
            }
        }
        if oui_data.contains_key(&mac_digit) {
            println!("{} {}", mac, oui_data.get(&mac_digit).unwrap());
        } else {
            println!("{} unknown", mac);
        }
    }
}
