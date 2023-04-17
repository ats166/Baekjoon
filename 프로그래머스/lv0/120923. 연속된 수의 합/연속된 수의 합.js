function solution(num, total) {
  var answer = [];
  let isEven, standard;

  if (num % 2 == 0) {
    isEven = true;
  } else {
    isEven = false;
  }

  if (isEven) {
    standard = (total - num / 2) / num;
  } else {
    standard = total / num;
  }

  if (isEven) {
    for (let i = standard - num / 2 + 1; i <= standard + num / 2; i++) {
      answer.push(i);
    }
  } else {
    for (
      let i = standard - Math.floor(num / 2);
      i <= standard + Math.floor(num / 2);
      i++
    ) {
      answer.push(i);
    }
  }
  return answer;
}