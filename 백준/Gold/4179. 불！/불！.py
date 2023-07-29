from collections import deque
import sys

input = sys.stdin.readline

# while True:
N,M = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(N)]
q = deque([])
result = []
flag = False


for j in range(N):
    for i in range(M):
        if arr[j][i] == 'J':
            arr[j][i] = 1
            q.append([j,i])

for j in range(N):
    for i in range(M):
        if arr[j][i] == 'F':
            q.append([j,i])

def bfs():
    global result, flag
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    while q:
        if result != []:
            break
        y,x = q.popleft()

        # for l in range(N):
        #     print(arr[l])
        # print('-------------',y,x,arr[y][x])

        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x

            if (dy < 0 or dy >= N or dx < 0 or dx >= M) and arr[y][x] != 'F':
                result.append(arr[y][x])
                flag = True
                break
            if dy < 0 or dy >= N or dx < 0 or dx >= M or arr[dy][dx] == '#':
                continue
            if arr[dy][dx] == '.' and arr[y][x] != 'F':
                arr[dy][dx] = arr[y][x] + 1
                # if dy == N-1 or dx == M-1 or dy == 0 or dx == 0:
                    # result = arr[dy][dx]
                    # print(result,'result')
                    # break
                q.append([dy,dx])

            elif arr[dy][dx] == 'F' or arr[y][x] != 'F':
                continue

            else:
                arr[dy][dx] = 'F'
                q.append([dy,dx])

bfs()

# for i in range(N):
#     print(arr[i])
if flag:
    print(min(result))
else:
    print('IMPOSSIBLE')