function solution(numbers, direction) {
    var answer = [];
    
    if (direction == "right") {
        for (let i =0; i<numbers.length; i++) {
            if ( i == numbers.length-1) {
                answer[0] = numbers[i]
            } else {
                answer [i+1] = numbers[i]
            }
        }
    } else {
        for (let i = numbers.length; i > -1; i--) {
            if ( i == 0 ) {
                answer[numbers.length-1] = numbers[0]
            } else {
                answer [i-1] = numbers[i]
            }
        }
    }
    return answer;
}