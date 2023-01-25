fn kaprekarNumbers(p: i32, q: i32) {
    let digit_count = | number | -> u32 {
        ((number as f64 + 0.1).log10()/2.0).ceil() as u32
    };
    let mut result : Vec<i64> = Vec::new();
    
    for i in p..q+1 {
        let i = i as i64;
        let sq :i64 = i * i;
        let dc :u32 = digit_count(sq);
        let slit :i64 = 10_i32.pow(dc) as i64;
        let prefix :i64 = sq / slit ;
        let suffix :i64 = sq - ( prefix * slit);
        if prefix + suffix == i{
            result.push(i);
        }
    }
    if result.len() > 0 {
        for r in result{
            print!("{} ", r);  
        }
    } else {
        println!( "INVALID RANGE");
    }
}
