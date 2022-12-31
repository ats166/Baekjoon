function solution(n) {
    let answer = [];
    let arr = [];

    for (let i = 0; i < n+1; i++) {
        arr[i] = i;
        if (arr[i] % 2 == 1) {
            answer.push(i)
        }
    }

    return answer;
}