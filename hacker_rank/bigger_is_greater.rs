fn biggerIsGreater(w: &str) -> String {
    // find from slice from right part
    // if w[i] > w[i-1] cut the slice
    // find to lowest char greater then w[i-1]
    // change their position
    // sort w[i..end]

    let mut w_: Vec<u8> = w.as_bytes().to_vec();
    for i in (1..w.len()).rev(){
        if w_[i] > w_[i-1]{
            let mut lowest_greatest: usize = i;
            for j in i+1..w.len(){
                if w_[lowest_greatest] > w_[j] && w_[j] > w_[i-1]  {
                    lowest_greatest = j;
                }
            }
            let hold = w_[lowest_greatest];
            w_[lowest_greatest] = w_[i-1];
            w_[i-1] = hold;
            w_[i..].sort_by(|a,b| a.cmp(b));
            return String::from_utf8(w_).unwrap();
        }        
    }
    return String::from("no answer")
}

