function solution(box, n) {
    var answer = 0;
    if (box[0] >= n && box[1] >= n && box[2] >= n) {
        answer = parseInt(box[0]/n) * parseInt(box[1]/n) * parseInt(box[2]/n)
    }
    return answer;
}