def solution(arr, computers):
    global answer
    answer = 0
    N = len(computers)
    used = [0] * N
    
    def dfs(j):
        for i in range(N):
            if computers[j][i] == 1 and used[i] == 0:
                used[i] = 1
                dfs(i)
        
    
    
    for j in range(N):
        if used[j] == 0:
            used[j] = 1
            answer += 1
            dfs(j)
            
            
    return answer