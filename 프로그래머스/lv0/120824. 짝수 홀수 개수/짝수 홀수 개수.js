function solution(num_list) {
    var answer = [0,0];
    
    num_list.map((num) => {
        if (num % 2 == 1) {
            return answer[1] += 1
        } else {
            return answer[0] += 1
        }
    })
    return answer;
}