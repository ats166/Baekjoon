def solution(brown, yellow):
    answer = []
    count = brown + yellow
    g = 3
    flag = False
    while True:
        
        for s in range(3,g+1):
            if g*s == count and ((g-2)*(s-2)) == yellow:
                answer.append(g)
                answer.append(s)
                flag = True
                break
        
        if flag:
            break
        g += 1
    return answer