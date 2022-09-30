from collections import deque

M,N = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
q = deque()
Max = -21e8
for j in range(N):
    for i in range(M):
        if arr[j][i] == 1:
            q.append([j,i])
            used[j][i] = 1

def bfs():
    global Max
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    while q:
        y,x = q.popleft()
        if arr[y][x] > Max:
            Max = arr[y][x]

        for k in range(4):

            dy = directy[k] + y
            dx = directx[k] + x

            if dy >= N or dy < 0 or dx >= M or dx < 0:
                continue
            if arr[dy][dx] == -1:
                continue
            if used[dy][dx] == 0:
                used[dy][dx] = 1
                arr[dy][dx] = arr[y][x] + 1
                q.append([dy,dx])


bfs()
flag = 0
for j in range(N):
    for i in range(M):
        if arr[j][i] == 0:
            flag = 1

if flag == 1:
    print("-1")
else:
    print(Max-1)