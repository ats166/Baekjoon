from collections import deque
import sys
input = sys.stdin.readline # 인풋 입력시간 줄이기

N,M = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(N)]
q = deque([])
result = []

for j in range(N): # 지훈이부터 움직여야되니까 지훈이 위치부터 찾기
    for i in range(M):
        if arr[j][i] == 'J':
            arr[j][i] = 1 # 지훈이는 턴수로 초기화
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
        if result != []: # 지훈이가 탈출했다면 bfs 탈출
            break
        y,x = q.popleft()

        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x
            
            if (dy < 0 or dy >= N or dx < 0 or dx >= M) and arr[y][x] != 'F': # 턴이 시작하기전 불이 아닌것이(지훈이) 밖으로 나간다면 result에 값을 넣어줌으로써 탈출여부 확인
                result.append(arr[y][x])
                break # 턴 시작전 탈출이 가능하다면 턴을 진행하지 않음
                
            if dy < 0 or dy >= N or dx < 0 or dx >= M or arr[dy][dx] == '#': # 배열 밖으로 벗어나거나 벽에 가로막히면 가지 않음
                continue
                
            if arr[dy][dx] == '.' and arr[y][x] != 'F': # 지나갈수 있는 공간이면서 현재 위치가 불이 아니라면(지훈이) 도착위치에 턴 초기화
                arr[dy][dx] = arr[y][x] + 1
                q.append([dy,dx])

            elif arr[dy][dx] == 'F' or arr[y][x] != 'F': # 현재 위치가 불이 아니거나(지훈이) 가야할 위치가 지점이 불이라면 탐색하지않음 (중복 탐색 방지)
                continue

            else:   # 걸러지고 남은것들은 전부 불이 이동할 수 있는 위치뿐
                arr[dy][dx] = 'F'
                q.append([dy,dx])

bfs()

if result != []:
    print(min(result))
else:
    print('IMPOSSIBLE')