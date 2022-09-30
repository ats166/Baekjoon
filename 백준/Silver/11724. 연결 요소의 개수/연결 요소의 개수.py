from collections import deque
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
arr = [[0] * V for _ in range(V)]
used = [0]*V
cnt = 0

for i in range(E):
    y,x = map(int,input().split())

    arr[y-1][x-1] = 1
    arr[x-1][y-1] = 1

def bfs(now):
    q = deque()
    q.append(now)

    while q:
        node = q.popleft()
        for i in range(V):
            if arr[node][i] == 1 and used[i] == 0:
                used[i] = 1
                q.append(i)

for j in range(V):
    flag = 0
    for i in range(V):
        if arr[j][i] == 1:
            flag = 1
            if used[j] == 0:
                used[j] = 1
                cnt += 1
                bfs(j)
    if flag == 0:
        cnt += 1

print(cnt)