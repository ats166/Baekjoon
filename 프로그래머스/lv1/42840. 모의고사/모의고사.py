def solution(answers):
    n = len(answers)//10
    answer = []
    
    a = [1,2,3,4,5,1,2,3,4,5] * (n+1)
    b = [2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5] * (n+1)
    c = [3,3,1,1,2,2,4,4,5,5] * (n+1)
    
    correct = {'1':0,'2':0,'3':0}
    
    for i in range(len(answers)):
        if a[i] == answers[i]:
            correct['1'] += 1
        if b[i] == answers[i]:
            correct['2'] += 1
        if c[i] == answers[i]:
            correct['3'] += 1
    
    mmax = max(correct.values())
    
    for k in correct:
        if correct[k] == mmax:
            answer.append(int(k))
    
    
    return answer