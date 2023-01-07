function solution(age) {
    let str = String(age)
    var answer = '';
    
    for (let i=0; i<str.length; i++) {
        answer += String.fromCharCode(Number(str[i])+97)
    }
    
    return answer;
}