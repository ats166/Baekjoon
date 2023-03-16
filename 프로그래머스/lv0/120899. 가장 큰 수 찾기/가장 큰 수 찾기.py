def solution(array):
    answer = []
    tmp = 0
    idx = 0
    for i in range(len(array)):
        if tmp <= array[i]:
            tmp = array[i]
            idx = i
    
    answer.append(tmp)
    answer.append(idx)
            
    return answer