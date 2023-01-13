function solution(numbers, k) {
    var answer = 0;
    let target = 0;
    
    for (let i =0; i < k-1; i++) {
        target += 2;
        if (target > numbers.length) {
            target -= numbers.length;
        }
    }
    
    return numbers[target];
}