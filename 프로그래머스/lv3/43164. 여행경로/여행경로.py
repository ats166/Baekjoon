import copy

def solution(tickets):
    global result
    answer = []
    n = len(tickets)
    used = [0] * (n+1)
    path = []
    result = ["ZZZ"] * n
    
    def dfs(level,end):
        global result
        if level == n-1:
            
            for l in range(1,n):
                if path[l] > result[l]:
                    break
                if path[l] < result[l]:
                    result = copy.deepcopy(path)
                    break
            return
            
        
        for k in range(n):
            if tickets[k][0] == end and used[k] == 0:
                used[k] = 1
                path.append(tickets[k][1])
                dfs(level+1,tickets[k][1])
                path.pop()
                used[k] = 0
    
    for i in range(n):
        if tickets[i][0] == "ICN":
            used[i] = 1
            path.append(tickets[i][0])
            path.append(tickets[i][1])
            dfs(0,tickets[i][1])
            path.remove(tickets[i][0])
            path.remove(tickets[i][1])
            used[i] = 0
    
    return result