function solution(array) {
    
    array.sort((a,b) => a-b);
    let idx = parseInt(array.length/2);
    

    return array[idx];
}