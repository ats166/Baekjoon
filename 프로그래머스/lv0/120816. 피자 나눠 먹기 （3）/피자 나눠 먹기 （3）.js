function solution(slice, n) {
    var answer = 0;
    
    answer = parseInt(n / slice);
    
    if (n % slice >= 1) {
        answer += 1;
    }
    
    return answer;
}