import copy
def solution(k, dungeons):
    global mmax
    answer = -1
    origin = copy.deepcopy(k)
    used = [0] * len(dungeons)
    path = [0] * len(dungeons)
    mmax = 0
    
    def dfs(level,k):
        global mmax
        if level == len(dungeons):
            count = 0
            k = copy.deepcopy(origin)
            for i in path:
                if dungeons[i][0] <= k:
                    count += 1
                    k -= dungeons[i][1]
                else:
                    break
            if count > mmax:
                mmax = copy.deepcopy(count)
            return
        
        for j in range(len(dungeons)):
            if used[j] == 0:
                used[j] = 1
                path[level] = j
                dfs(level+1,k)   
                used[j] = 0
    
    dfs(0,k)
    
    return mmax