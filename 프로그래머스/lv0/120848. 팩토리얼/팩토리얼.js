function solution(n) {
    var answer = 0;
    let tmp = 1;
    for (let i=10; i>0; i--) {
        for ( let j=i; j>0; j--) {
            tmp *= j;
        }
        if (tmp <= n) {
            answer = i;
            break;
        }
        tmp = 1;
    }
    return answer;
}