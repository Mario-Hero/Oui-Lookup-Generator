use std::env;
use phf::phf_map;


static OUI_DATA: phf::Map<&'static str, &'static str> = phf_map! {
    // ***insert_point***
    "286FB9" => "Nokia Shanghai Bell Co., Ltd.",
    // ***insert_point***
};


fn main() {
    let args: Vec<String> = env::args().collect();
    for mac in args.iter().skip(1) {
        let mut mac_alpha = String::new();
        let mut add_times: u32 = 0;
        for c in mac.chars() {
            if c.is_alphanumeric() {
                mac_alpha.push(c.to_ascii_uppercase());
                add_times += 1;
                if add_times >= 6 {
                    break;
                }
            }
        }
        if OUI_DATA.contains_key(&mac_alpha) {
            println!("{} {}", mac, OUI_DATA.get(&mac_alpha).unwrap());
        } else {
            println!("{} unknown", mac);
        }
    }
}
