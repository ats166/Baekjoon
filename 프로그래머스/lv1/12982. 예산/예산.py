def solution(d, budget):
    cal = 0
    d.sort()
    answer = 0
    if sum(d) <= budget :
        answer = len(d)
    else:
        for i in range(len(d)):
            cal += d[i]
            if cal == budget:
                answer = i+1
                break
            elif cal > budget:
                answer = i
                break
    
    return answer