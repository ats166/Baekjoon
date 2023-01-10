function solution(hp) {
    var answer = 0;
    
    while (hp) {
        if (hp >= 5) {
            hp -= 5;
            answer += 1
        }
        else if (hp >= 3) {
            hp -= 3;
            answer += 1;
        } else {
            hp -= 1;
            answer += 1
        }
    }
    return answer;
}