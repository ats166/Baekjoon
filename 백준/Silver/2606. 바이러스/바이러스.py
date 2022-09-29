N = int(input())
M = int(input())

arr = [[0]*N for _ in range(N)]
used = [0] * N
cnt = 0

for i in range(M):
    y,x = map(int,input().split())

    arr[y-1][x-1] = 1
    arr[x-1][y-1] = 1

def dfs(now):
    global cnt

    for i in range(N):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            cnt += 1
            dfs(i)

used[0] = 1
dfs(0)
print(cnt)