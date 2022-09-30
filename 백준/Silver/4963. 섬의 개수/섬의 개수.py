from collections import deque

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0

    def bfs(j,i):
        q = deque([(j,i)])

        directy = [-1,-1,-1,0,0,1,1,1]
        directx = [-1,0,1,-1,1,-1,0,1]

        while q:
            y,x = q.popleft()

            for k in range(8):
                dy = directy[k] + y
                dx = directx[k] + x

                if dy >= h or dy < 0 or dx >= w or dx < 0:
                    continue
                if arr[dy][dx] == 1:
                    arr[dy][dx] = 0
                    q.append([dy,dx])

    for j in range(h):
        for i in range(w):
            if arr[j][i] == 1:
                cnt += 1
                arr[j][i] = 0
                bfs(j,i)

    print(cnt)