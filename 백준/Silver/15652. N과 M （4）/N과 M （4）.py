N,M = map(int,input().split())

path = [0] * M

def dfs(st,level):

    if level == M:
        flag = 0
        for i in range(M-1):
            if path[i] > path[i+1]:
                flag = 1
        if flag == 0:
            print(*path)
            return
        return

    for i in range(st,N+1):
        path[level] = i
        dfs(st,level+1)


dfs(1,0)