from collections import deque

M,N,H = map(int,input().split())
tomato = []
q = deque()
directy = [-1,1,0,0,0,0]
directx = [0,0,1,-1,0,0]
directk = [0,0,0,0,-1,1]
mmax = 0
used = [[[0] * M for _ in range(N)] for _ in range(H)]

for j in range(H):
    arr = []
    for i in range(N):
        tmp = list(map(int,input().split()))
        arr.append(tmp)
    tomato.append(arr)

# print(tomato)

for k in range(H):
    for j in range(N):
        for i in range(M):
            if tomato[k][j][i] == 1:
                used[k][j][i] = 1
                q.append([k,j,i])
# print(q)

def bfs():
    global mmax

    while q:
        k,y,x = q.popleft()
        # print(y,x,k)

        for l in range(6):
            dy = directy[l] + y
            dx = directx[l] + x
            dk = directk[l] + k

            if dy >= N or dy < 0 or dx >= M or dx < 0 or dk >= H or dk < 0:
                continue
            if tomato[dk][dy][dx] == -1:
                continue
            # print(dk,dy,dx,'a',k,y,x,'b',l)
            if used[dk][dy][dx] == 0:
                used[dk][dy][dx] = 1
                tomato[dk][dy][dx] = tomato[k][y][x] + 1
                if mmax < tomato[dk][dy][dx]:
                    mmax = tomato[dk][dy][dx]
                q.append([dk,dy,dx])


bfs()

# for i in range(3):
#     print(*tomato[0][i])
# print()
#
# for i in range(3):
#     print(*tomato[1][i])
flag = 0
for k in range(H):
    for j in range(N):
        for i in range(M):
            if tomato[k][j][i] == 0:
                flag = 1

if flag:
    print(-1)
else:
    if mmax == 0:
        print(0)
    else:
        print(mmax-1)
