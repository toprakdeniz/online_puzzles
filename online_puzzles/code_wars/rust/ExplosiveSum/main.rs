use std::collections::Hashmap

struct ExpSum {
    cache: Hashmap<(u64, u64), u64>
}

impl ExpSum {

    fn new() {
        ExpSum{
            cache: Hashmap::new()
        }
    }


    fn exp_mid(mut self, n: u64, base_level_element_count: u64) -> u64 {
        // bug 
        let upper_remainders = n - base_level_element_count;
        let full_max: u64 = (upper_remainders/ base_level_element_count).floor();
        let remainder: u64 = upper_remainders % base_level_element_count;
        let mut result = 0;
        if not self.cache.contains_key(upper_remainders){
            todo!("calculate")
        }
        result += self.cache.get(upper_remainders) * full_max;
        if not self.cache.contans_key(remainder){
            todo!("calculate")
        }
        result += self.cache.get(remainder);
    }
    
    
    fn exp_sum(n: u64) -> 64 {

    }

}



