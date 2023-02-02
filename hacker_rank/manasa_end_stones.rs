fn stones(n: i32, a: i32, b: i32) -> Vec<i32> {
    // n lenght of combination
    // a,b items to be combined
    use std::collections::BinaryHeap;
    use std::cmp::Reverse;
    let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
    for i in 0..n{
        heap.push( Reverse( a*i + b*(n-i-1)));
    }
    let mut result: Vec<i32> = Vec::new();
    let mut last = 0;
    for _ in 0..n{
        let Reverse(current) = heap.pop().unwrap();
        if current != last  {
                last = current;
                result.push(current);
            }
        }
    result
}
