import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N,M,R = map(int,input().split())

arr = [[] for _ in range(N)]
used = [0] * N
cnt = 0

for i in range(M):
    a,b = map(int,input().split())

    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

def dfs(node):
    global cnt
    cnt += 1
    used[node] = cnt
    arr[node].sort()

    for k in arr[node]:
        if used[k] == 0:
            dfs(k)


dfs(R-1)
for i in range(N):
    print(used[i])