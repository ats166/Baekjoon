N,M = map(int,input().split())
used = [0] * (N+1)
path = [0] * M

def dfs(st,level):

    if level == M:
        print(*path,end =' ')
        print()
        return

    for i in range(st,N+1):
        if used[i] == 0:
            used[i] = 1
            path[level] = i
            dfs(i+1,level+1)
            used[i] = 0

dfs(1,0)