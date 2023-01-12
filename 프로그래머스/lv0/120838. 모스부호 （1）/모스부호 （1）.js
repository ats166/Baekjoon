function solution(letter) {
    var answer = '';
    let tmp = '';
    let morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    for (let i =0; i<letter.length; i++) {
        if (letter[i] == ' ') {
            console.log(answer,tmp);
            answer+=morse[tmp];
            tmp = [];
        } else {
            tmp += letter[i];
        }
    }
    answer += morse[tmp]
    return answer
}