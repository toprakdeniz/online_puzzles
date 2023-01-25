fn gridSearch(G: &[String], P: &[String]) -> String {
    for i in 0..G.len() - P.len() + 1 {
        let place = G[i].match_indices(&P[0]);
        match place {
          Some(m) => {
              let mut found = true;
              for j in 1..P.len() {
                  let place_others = G[i+j].match_indices(&P[j]);
                  match place_others {
                      Some(m) => {continue;},
                      Some(n) => {
                          if n < m {
                                found = false;
                                break;
                          } else {
                              
                          }
                      }
                  } Some(m){

                  }
              }
              if found {
                  return String::from("YES");
              }
          },
          _ => {} 
        };
    }
    return String::from("NO");
}
