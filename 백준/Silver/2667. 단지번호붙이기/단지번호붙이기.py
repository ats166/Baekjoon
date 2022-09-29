from collections import deque

N = int(input())

arr=[list(map(int,input())) for _ in range(N)]
cnt = 0
result = []
def bfs(y,x):
    q = deque([(y,x)])
    tmp = 1
    arr[y][x] = 0

    while q:
        y,x = q.popleft()

        directy = [-1,1,0,0]
        directx = [0,0,-1,1]

        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x

            if dy >= N or dy < 0 or dx >= N or dx < 0:
                continue
            if arr[dy][dx] == 1:
                tmp += 1
                arr[dy][dx] = 0
                q.append([dy,dx])
    result.append(tmp)

for j in range(N):
    for i in range(N):
        if arr[j][i] == 1:
            cnt += 1
            bfs(j,i)

print(cnt)
result.sort()

for i in range(len(result)):
    print(result[i])