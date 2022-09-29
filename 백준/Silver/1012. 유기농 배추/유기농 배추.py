from collections import deque
TC = int(input())

for tc in range(1,TC+1):
    M,N,V = map(int,input().split())

    arr = [[0] * M for _ in range(N)]
    for i in range(V):
        x,y = map(int,input().split())

        arr[y][x] = 1
    cnt = 0

    def bfs(y,x):

        q = deque([(y,x)])

        while q:
            y,x = q.popleft()

            directy = [0,0,1,-1]
            directx = [1,-1,0,0]

            for k in range(4):
                dy = directy[k] + y
                dx = directx[k] + x

                if dy >= N or dy < 0 or dx >= M or dx < 0:
                    continue
                if arr[dy][dx] == 1:
                    arr[dy][dx] = 0
                    q.append([dy,dx])

    for j in range(N):
        for i in range(M):
            if arr[j][i] == 1:
                cnt += 1
                arr[j][i] = 0
                bfs(j,i)

    print(cnt)