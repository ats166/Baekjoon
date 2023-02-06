function solution(order) {
    var answer = 0;
    let result_order = String(order)
    let new_order = result_order.split("");
    
    console.log(new_order.length)
    for (let i=0; i<new_order.length; i++ ) {
        if (new_order[i] == 3 || new_order[i] == 6 || new_order[i] == 9) {
            answer += 1;
        }
    }
    return answer;
}