from collections import deque
import sys
input = sys.stdin.readline

M,N,K = map(int,input().split())

arr = [[0] * N for _ in range(M)]

for _ in range(K):
    a,b,c,d = map(int,input().split())
    for j in range(a, c):
        for i in range(M-d,M-b):
            arr[i][j] = 1

def bfs(j,i):
    global cnt

    directy = [-1,1,0,0]
    directx = [0,0,1,-1]

    q = deque([(j, i)])

    while q:
        y, x = q.popleft()

        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x

            if dy < 0 or dy >= M or dx < 0 or dx >= N:
                continue
            if arr[dy][dx] == 0:
                arr[dy][dx] = 5
                cnt += 1
                q.append([dy, dx])

result = []
count = 0

for j in range(M):
    for i in range(N):
        if arr[j][i] == 0:
            cnt = 1
            count += 1
            arr[j][i] = 5
            bfs(j,i)
            result.append(cnt)

result = sorted(result)

print(count)
for i in range(len(result)):
    print(result[i], end = ' ')