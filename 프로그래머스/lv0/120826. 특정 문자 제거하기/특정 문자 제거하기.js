function solution(my_string, letter) {
    var answer = '';
    
    [...my_string].forEach((string) => {
        if (string != letter) {
            answer += string
        }
    })
    
    return answer;
}