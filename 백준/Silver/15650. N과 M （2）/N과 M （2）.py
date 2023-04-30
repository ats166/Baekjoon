N, M = map(int,input().split())
path = [0] * M
used = [0] * N

def dfs(st,level):

    if level == M:
        print(*path, sep=' ')
        return

    for i in range(st,N):
        if used[i] == 0:
            used[i] = 1
            path[level] = i + 1
            dfs(i+1, level+1)
            used[i] = 0


dfs(0,0)