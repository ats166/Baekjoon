function solution(num_list, n) {
    var answer = [];
    let tmp = [];
    
    for (let i =0; i<num_list.length; i+=n) {
        for (let j = 0; j<n; j++) {
            tmp[j] = num_list[i+j];
        }
        answer.push(tmp);
        tmp = [];
    }
    return answer;
}