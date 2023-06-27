def solution(elements):
    n = len(elements)
    elements = elements * 2
    answer = set()
    
    for k in range(n):
        num = sum(elements[:k+1])                                                                          
        answer.add(num)
        for j in range(k,n+k):
            num -= elements[j-k]
            num += elements[j+1]
            if num not in answer:
                answer.add(num)
        
    return len(answer)