def solution(numbers, target):
    global answer
    answer = 0
    n = len(numbers)
    used = [0] * n
    result = 0
    
    def dfs(level,result,st):
        global answer

        
        if level == n:
            if result == target:
                answer += 1
            return
        else:
            dfs(level+1, result+numbers[level], level)
            dfs(level+1, result-numbers[level], level)
        
        
    dfs(0,result,0)
    return answer