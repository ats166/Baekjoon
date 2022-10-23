N,M = map(int,input().split())
path = [''] * M
used = [0] * N
def dfs(level):

    if level == M:
        for i in range(M):
            print(path[i], end = ' ')
        print()
        return

    for j in range(N):
        if used[j] == 0:
            used[j] = 1
            path[level] = j+1
            dfs(level+1)
            used[j] = 0

dfs(0)