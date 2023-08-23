fn build_path(mut map: Vec<Vec<i8>>, size: usize) -> Vec<Vec<i8>>{
    let mut l = 0; let mut r = size -1; let mut t = 0; let mut b = size - 1;
    let mut x = 0;
    let mut y = 1;
    
    while x <= r && y <= b {
        // go right
        while x < r {
            map[y][x] = 0;
            x += 1;
        }
        x -= 1;
        y += 1;
        t += 2;
        // go down
        while y < b {
            map[y][x] = 0;
            y += 1;
        }
        y -= 1;
        x -= 1;
        r -= 2;
        // go left
        while x > l {
            map[y][x] = 0;
            x -= 1;
        }
        x += 1;
        y -= 1;
        b -= 2;
        // go up
        while y > t {
            map[y][x] = 0;
            y -= 1;
        }
        y += 1;
        x += 1;
        l += 2;
    }

    return map;
}


fn spiralize(size: usize) -> Vec<Vec<i8>> {
    let mut map: Vec<Vec<i8>> = vec![];
    for _ in 0..size {
        let row: Vec<i8> = vec![1; size];
        map.push(row);
    }
    build_path(map, size)
}


fn main(){
    let map = spiralize(8);
    for row in map {
        println!("{:?}", row);
    }
}

// assertion failed: `(left == right)`
//   left: `[[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]`,
//  right: `[
//     [1, 1, 1, 1, 1, 1], 
//     [0, 0, 0, 0, 0, 1], 
//     [1, 1, 1, 1, 0, 1], 
//     [1, 0, 0, 1, 0, 1], 
//     [1, 0, 0, 0, 0, 1], 
//     [1, 1, 1, 1, 1, 1]]`: spiralize(6)