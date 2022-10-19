import copy
from collections import deque

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
acc = copy.deepcopy(arr)
directy = [-1,1,0,0]
directx = [0,0,-1,1]

def bfs(y,x):
    q = deque([(y,x)])
    arr[y][x] = False

    while q:
        y,x = q.popleft()

        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x

            if dy >= N or dy < 0 or dx >= N or dx < 0:
                continue
            if arr[dy][dx] != False:
                arr[dy][dx] = False
                q.append([dy,dx])

result = []
for l in range(101):
    arr = copy.deepcopy(acc)
    used = [[0]*N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for i in range(N):
            if arr[j][i] <= l:
                arr[j][i] = False

    for j in range(N):
        for i in range(N):
            if arr[j][i] != False:
                bfs(j,i)
                cnt += 1

    result.append(cnt)

    if cnt == 0:
        break

print(max(result))