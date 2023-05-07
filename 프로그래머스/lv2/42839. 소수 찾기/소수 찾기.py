def solution(numbers):
    global answer
    answer = 0
    N = len(numbers)
    prime = [True] * 10000001
    prime[0], prime[1] = False,False
    
    n = int(10000001 ** 0.5)
    for i in range(2,n+1):
        if prime[i] == True:
            for j in range(i+i, 10000001, i):
                prime[j] = False
    
    number = list(numbers)
    used = [0] * N
    path = []
    visited = []
    
    def dfs(level):
        global answer
        if level >= 1:
            tmp = ""
            for k in range(len(path)):
                tmp += path[k]
            if int(tmp) not in visited:
                visited.append(int(tmp))
                if prime[int(tmp)]:
                    answer += 1
        
        if level == N:
            return
        
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                path.append(number[i])
                dfs(level+1)
                path.remove(number[i])
                used[i] = 0
        
    dfs(0)
    return answer