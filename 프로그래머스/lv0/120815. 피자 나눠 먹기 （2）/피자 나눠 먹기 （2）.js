function solution(n) {
    var answer = 0;
    let piece = 6;
    let flag = 1;
    let check = n;
    
    while (flag) {
        if (n == piece) {
            flag = 0;
        } else if (n > piece) {
            piece += 6;
        } else {
            n += check;
        }
    }
    
    return n/6;
}