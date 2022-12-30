fn kaprekarNumbers(p: i32, q: i32) {
    let digit_count = | number | -> u32 {
        ((number as f64 + 0.1).log10()/2.0).ceil() as u32
    };
    let mut result : Vec<i32> = Vec::new();
    
    for i in p..q+1 {
        let sq :i32 = i * i;
        let dc :u32 = digit_count(sq);
        let slit :i32 = 10_i32.pow(dc) as i32;
        let prefix :i32 = sq / slit ;
        let suffix :i32 = sq - ( prefix * slit);
        if prefix + suffix == i {
            result.push(i);
        }
    }
    for r in result{
     print!("{} ", r);  
    }
}
