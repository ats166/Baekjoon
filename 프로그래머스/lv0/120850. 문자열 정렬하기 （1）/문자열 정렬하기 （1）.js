function solution(my_string) {
    var answer = [];
    let my = [...my_string]
    for (let i=0; i<my.length; i++) {
        if (isNaN(my[i])) {
            console.log('hi')
        } else {
            answer.push(parseInt(my[i]))
        }
    }
    
    return answer.sort();
}