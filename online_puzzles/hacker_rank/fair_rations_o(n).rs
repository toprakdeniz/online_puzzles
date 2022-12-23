fn fairRations(B: &[i32]) -> String {
    let mut loaves: i32 = 0;
    let mut odd: bool = false;
    for b in B{
        match (b%2, odd) {
            (0, true) => { loaves = loaves + 2;},
            (0, false) => {},
            (1, true) => { odd = false;},
            (1, false) => { loaves = loaves + 2;
                            odd = true;},
            _ => {}
        };
    }
    match odd {
        true => String::from("NO"),
        false => loaves.to_string()
    }
}

