from collections import deque

N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
directy = [-1,1,0,0]
directx = [0,0,-1,1]

def bfs(y,x):

    q = deque([(y,x)])
    while q:
        y,x = q.popleft()
        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x

            if dy >= N or dy < 0 or dx >= M or dx < 0:
                continue
            if arr[dy][dx] == 1 and used[dy][dx] == 0:
                used[dy][dx] = 1
                arr[dy][dx] = arr[y][x] + arr[dy][dx]
                q.append([dy,dx])

used[0][0] = 1
bfs(0,0)
print(arr[-1][-1])