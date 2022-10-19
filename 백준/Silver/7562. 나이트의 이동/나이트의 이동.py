from collections import deque
TC = int(input())

for tc in range(TC):
    N = int(input())
    used = [[0]*N for _ in range(N)]

    arr = [[-5]*N for _ in range(N)]
    y,x = map(int,input().split())
    used[y][x] = 1
    arr[y][x] = 0
    q = deque([(y,x)])
    j,i = map(int,input().split())
    arr[j][i] = 'ed'
    directy = [-1,-2,-2,-1,1,2,2,1]
    directx = [-2,-1,1,2,-2,-1,1,2]
    result = 0

    def bfs():
        global result,q
        while q:
            y,x = q.popleft()

            for k in range(8):

                dy = directy[k] + y
                dx = directx[k] + x

                if dy >= N or dy < 0 or dx >= N or dx < 0:
                    continue
                if arr[dy][dx] == 'ed':
                    result = arr[y][x] + 1
                    q=[]
                    break
                if used[dy][dx] == 0:
                    used[dy][dx] = 1
                    arr[dy][dx] = arr[y][x] + 1
                    q.append([dy,dx])


    if j == y and i == x:
        print("0")
    else:
        bfs()
        print(result)