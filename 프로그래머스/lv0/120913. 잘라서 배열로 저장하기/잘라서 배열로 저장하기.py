def solution(my_str, n):
    answer = [] 
    for i in range(0,len(my_str),n):
        tmp = ""
        for j in range(n):
            if i+j >= len(my_str):
                break
            tmp += my_str[i+j]
        answer.append(tmp)
    return answer