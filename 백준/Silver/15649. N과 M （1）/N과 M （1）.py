import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
used = [0] * N
result = [0] * M

def dfs(level):

    if level == M:
        print(*result, sep=' ')
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            result[level] = i+1
            dfs(level+1)
            used[i] = 0

dfs(0)