def solution(s1, s2):
    answer = 0
    
    for j in range(len(s1)):
        for i in range(len(s2)):
            if s1[j] == s2[i]:
                answer += 1
    return answer