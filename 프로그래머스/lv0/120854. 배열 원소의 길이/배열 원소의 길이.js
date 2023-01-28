function solution(strlist) {
    var answer = [];
    
    for (let j = 0; j < strlist.length; j ++) {
        let tmp = [...strlist[j]];
        answer.push(tmp.length)
    }
    return answer;
}