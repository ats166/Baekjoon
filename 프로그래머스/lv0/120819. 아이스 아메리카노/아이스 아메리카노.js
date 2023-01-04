function solution(money) {
    var answer = [];
    let coffee = 0;
    
    
    while (money >= 5500) {
        money -= 5500;
        coffee += 1;
    }
    
    answer.push(coffee, money);
    
    return answer;
}