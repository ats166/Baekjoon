function solution(my_string) {
    var answer = 0;
    let my = [...my_string];
    
    for (let i =0; i<my.length; i++ ){
        if (!(isNaN(my[i]))) {
            answer += parseInt(my[i]);
        }
    }
    return answer;
}