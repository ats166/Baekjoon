def solution(my_string):
    answer = my_string.lower()
    answer = sorted(answer)
    result = ''
    for i in range(len(answer)):
        result += answer[i]
    return result