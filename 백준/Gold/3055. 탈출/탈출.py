from collections import deque

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
used = [[0] * M for _ in range(N)]
used2 = [[0] * M for _ in range(N)]
directy = [-1,1,0,0]
directx = [0,0,-1,1]
q = deque()
tmp1,tmp2 = [],[]
result,flag = 0,0
for j in range(N):
    for i in range(M):
        if arr[j][i] == 'S':
            tmp1 = [j,i,'S']
            arr[j][i] = 0
            used2[j][i] = 1
        if arr[j][i] == '*':
            tmp2.append([j,i,'*'])
            used[j][i] = 1
            flag += 1
        if arr[j][i] == 'D':
            used[j][i] = 1

q.append(tmp1)
for i in range(flag):
    q.append(tmp2[i])

def bfs():
    global result,q

    while q:
        y,x,s = q.popleft()

        for k in range(4):

            dy = directy[k] + y
            dx = directx[k] + x
            if dy >= N or dy < 0 or dx >= M or dx < 0 or arr[dy][dx] == 'X':
                continue
            if s == 'S':
                if arr[dy][dx] == 'D' and used[y][x] == 0:
                    result = arr[y][x] + 1
                    q = []
                    break
                if used2[dy][dx] == 0 and used[dy][dx] == 0 and used[y][x] == 0:
                    used2[dy][dx] = 1
                    arr[dy][dx] = arr[y][x] + 1
                    q.append([dy,dx,'S'])
            if s == '*':
                if used[dy][dx] == 0:
                    used[dy][dx] = 1
                    arr[dy][dx] = '*'
                    q.append([dy,dx,'*'])

bfs()

if result == 0:
    print("KAKTUS")
else:
    print(result)