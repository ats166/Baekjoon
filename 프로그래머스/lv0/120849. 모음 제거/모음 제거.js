function solution(my_string) {
    let mystring = [...my_string];
    let ahdma = ['a','e','i','o','u']
    let answer = mystring.map((string) => {
        if (ahdma.indexOf(string) == -1) {
            return string
        }
    })
    let result = '';
    for (let i =0; i<answer.length; i++) {
        if (answer[i] != null) {
            result += answer[i]
        }
    }
    return result;
}