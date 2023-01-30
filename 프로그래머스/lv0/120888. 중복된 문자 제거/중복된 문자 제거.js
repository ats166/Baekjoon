function solution(my_string) {
    var answer = [];
    let result = '';
    let my = [...my_string]
    
    for (let i =0; i<my.length; i++ ){
        let flag = 0;
        for (let j =0; j<answer.length; j++ ) {
            if (answer[j] == my[i]) {
                flag = 1;
            }
        }
        if (flag !== 1) {
            answer.push(my[i])
            }
    }
    for (let i=0; i<answer.length; i++ ) {
        result += answer[i]
    }
    return result;
}