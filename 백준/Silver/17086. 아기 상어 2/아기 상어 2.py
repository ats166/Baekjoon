import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
q = deque()
Max = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for j in range(N):
    for i in range(M):
        if arr[j][i] == 1:
            q.append([j,i])

def bfs():
    global Max
    directy = [-1,-1,-1,0,0,1,1,1]
    directx = [-1,0,1,-1,1,-1,0,1]

    while q:
        y,x = q.popleft()

        for k in range(8):
            dy = directy[k] + y
            dx = directx[k] + x

            if dy >= N or dy < 0 or dx >= M or dx < 0:
                continue
            elif arr[dy][dx] == 0:
                arr[dy][dx] = arr[y][x] + 1
                if arr[dy][dx] >= Max:
                    Max = arr[dy][dx]
                q.append([dy,dx])

bfs()

print(Max-1)