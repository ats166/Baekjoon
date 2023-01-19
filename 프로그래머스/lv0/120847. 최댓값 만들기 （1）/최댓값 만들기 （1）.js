function solution(numbers) {
    var answer = 0;
    // let max = Math.max(...numbers);
    // let max2 = -1;
    // for (let i=0; i<numbers.length; i++) {
    //     if (numbers[i] != max && max2 < numbers[i]) {
    //         max2 = numbers[i];
    //     }
    // }
    numbers.sort(function(a,b) {
        return a-b
    })
    return numbers[numbers.length-1] * numbers[numbers.length-2];
}