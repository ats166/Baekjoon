function solution(emergency) {
    var answer = [];
    let arr = new Array(emergency.length);
    let cnt = 1
    
    for (let j = 0; j<emergency.length; j++) {
        let max = 0;
        let idx = 0;
        for (let i = 0; i<emergency.length; i++) {
            if (emergency[i] >= max) {
                max = emergency[i];
                idx = i;
            }
        }
        emergency[idx] = 0;
        arr[idx] = cnt;
        cnt += 1;
    }
    return arr;
}