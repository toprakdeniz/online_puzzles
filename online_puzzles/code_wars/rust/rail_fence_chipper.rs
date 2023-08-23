fn encode_rail_fence_cipher(text: &str, num_rails: usize) -> String {
    let mut rails: Vec<Vec<char>> = vec![Vec::new(); num_rails];
    let mut forward = true;
    let mut i = 0;
    for c in text.chars() {
        rails[i].push(c);
        if forward {
            i += 1;
        } else {
            i -= 1;
        }
        if i == num_rails - 1 || i == 0 {
            forward = !forward;
        }
    }
    // collect rails into a single string
    rails.into_iter().flatten().collect::<String>()
}

fn decode_rail_fence_cipher(text: &str, num_rails: usize) -> String {
    println!("{}", text.len());
    let step_size = (num_rails -1) * 2;
    let remainer = text.len() % step_size;
    let fill_up = remainer < num_rails;
    let min_len = text.len() / step_size;

    let mut rail_lengths = vec![min_len; num_rails];
    (1usize .. num_rails -1).into_iter().for_each(|i| rail_lengths[i] *= 2);
    if fill_up {
        (0usize .. remainer).into_iter().for_each(|i| rail_lengths[i] += 1);
    } else {
        (remainer .. num_rails).into_iter().for_each(|i| rail_lengths[i] += 1);
    }
    println!("{:?}", rail_lengths);

    let mut rail_starts = rail_lengths.into_iter().scan(0, |sum, x| {
        let temp = *sum;
        *sum += x;
        Some(temp)
    }).collect::<Vec<usize>>();
    println!("{:?}", rail_starts);

    let mut result: Vec<char> = vec![];
    let mut i = 0;
    let mut index = 0;
    let mut forward = true;
    while i < text.len() {
        result.push(text.chars().nth(rail_starts[index]).unwrap());
        rail_starts[index] += 1;
        i += 1;
        if forward {
            index += 1;
        } else {
            index -= 1;
        }
        if index == num_rails - 1 || index == 0 {
            forward = !forward;
        }
    }
    result.into_iter().collect::<String>()
}

fn main() {
    // use std::env;
    // env::set_var("RUST_BACKTRACE", "full");
    // println!("{}", encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3));
    // println!("WECRLTEERDSOEEFEAOCAIVDEN");
    println!("{}", decode_rail_fence_cipher("abcde", 3));
    println!("-----");
    println!("{}", decode_rail_fence_cipher("abcde", 4));
    println!("-----");

    let rails = vec![vec!['a','a','a'], vec!['b','b','b'], vec!['c','c','c']];
    println!("{:?}", rails.into_iter().flatten().collect::<String>());
}