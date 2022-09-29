N,M,V = map(int,input().split())
arr = [[0]*N for _ in range(N)]

for i in range(M):
    y,x = map(int,input().split())
    arr[y-1][x-1] = 1
    arr[x-1][y-1] = 1

used = [0] * N

def dfs(level):
    print(level,end = ' ')
    for i in range(N):
        if used[i] == 0 :
            if arr[level-1][i] == 1:
                used[i] = 1
                dfs(i+1)

used[V-1] = 1
dfs(V)
print()
def bfs(now):
    node = [now]
    while node:
        y = node.pop(0)
        print(y+1,end = ' ')
        for i in range(N):
            if arr[y][i] == 1 and used[i] == 0:
                used[i] = 1
                node.append(i)

used = [0] * N
used[V-1] = 1
bfs(V-1)
