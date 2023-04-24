from collections import deque
import sys
input = sys.stdin.readline

N,M,V = map(int,input().split())

arr = [[0] * N for _ in range(N)]
used = [0] * N
for i in range(M):
    s,e = map(int,input().split())
    arr[s-1][e-1] = 1
    arr[e-1][s-1] = 1

def dfs(level):

    if used[level] == 0:
        print(level+1, end = ' ')
        used[level] = 1
        for j in range(N):
            if arr[level][j] == 1:
                dfs(j)

def bfs(level):
    node = deque([level])

    while node:
        y = node.popleft()
        print(y+1, end= ' ')
        for k in range(N):
            if used[k] == 0 and arr[y][k] == 1:
                used[k] = 1
                node.append(k)



dfs(V-1)
print()
used = [0] * N
used[V-1] = 1
bfs(V-1)