function solution(balls, share) {
    var answer = 0;
    
    let N = BigInt(1);
    let M = BigInt(1);
    let O = BigInt(1);
    
    for (let i =balls; i > 0; i-- ) {
        N *= BigInt(i)
    }
    for (let i =share; i > 0; i--) {
        M *= BigInt(i)
    }
    for (let i =balls-share; i > 0; i--) {
        O *= BigInt(i)
    }
    
    answer = N / (O*M)
    
    return answer;
}