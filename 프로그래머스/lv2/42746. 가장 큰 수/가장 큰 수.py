def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i]) * 4
    
    number = sorted(numbers, key= lambda x: (x[0], x[1], x[2], x[3]), reverse=True)
    
    for i in range(len(number)):
        answer += number[i][:len(number[i]) // 4]
        # answer += len(number[i]) // 3
    
    if int(answer) == 0:
        answer = "0"
    
    return answer