def solution(array):
    answer = 0
    for i in range(len(array)):
        tmp = str(array[i])
        for j in range(len(tmp)):
            if tmp[j] == "7":
                answer += 1
    return answer