

def solution(clothes):

    answer = 1
    tmp = 0
    
    combination = {}
    
    for i in range(len(clothes)):
        try:    
            combination[clothes[i][1]] += 1
        except:
            combination[clothes[i][1]] = 1
            
    result = list(combination.values())

    for j in range(len(result)):
        answer *= (result[j] + 1)
        print(answer, result[j]+1)
    
    return answer - 1