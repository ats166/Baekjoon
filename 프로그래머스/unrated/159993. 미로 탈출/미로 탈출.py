from collections import deque

def solution(maps):
    testcase = ["XXXXL", "XOOSX", "XXXXX", "XXXOO", "EXXXX", "XXXXX"]
    
    answer = 0
    N,M = len(maps), len(maps[0])
    print(N,M)
    arr = [[0] * M for _ in range(N)]
    brr = [[0] * M for _ in range(N)]
    
    for i in range(len(maps)):
        arr[i] = list(maps[i])
        brr[i] = list(maps[i])
        
    def bfs(j,i):
        directy = [-1,1,0,0]
        directx = [0,0,1,-1]
        
        q = deque([(j,i)])
        
        while q:
            y, x = q.popleft()

            for k in range(4):
                dy = directy[k] + y
                dx = directx[k] + x
                
                if dy >= N or dx >= M or dy < 0 or dx < 0:
                    continue
                
                if arr[dy][dx] == 'O' or arr[dy][dx] == 'E':
                    arr[dy][dx] = arr[y][x] + 1
                    q.append([dy,dx])
                if arr[dy][dx] == 'L':
                    q = []
                    return [arr[y][x] + 1, dy, dx]
    
    for j in range(N):
        for i in range(M):
            if arr[j][i] == 'S':
                arr[j][i] = 0
                flag = False
                flag = bfs(j,i)
                break
    
    def bfs2(j,i):
        directy = [-1,1,0,0]
        directx = [0,0,1,-1]
        
        q = deque([(j,i)])
        
        while q:
            y, x = q.popleft()

            for k in range(4):
                dy = directy[k] + y
                dx = directx[k] + x
                
                if dy >= N or dx >= M or dy < 0 or dx < 0:
                    continue
                
                if brr[dy][dx] == 'O' or brr[dy][dx] == 'S':
                    brr[dy][dx] = brr[y][x] + 1
                    q.append([dy,dx])
                if brr[dy][dx] == 'E':
                    q = []
                    return brr[y][x]+1
    
    print(arr)
    if flag:
        st,y,x = flag[0], flag[1], flag[2]
        brr[y][x] = st
        flag2 = False
        flag2 = bfs2(y,x)
        
        if flag2:
            answer = flag2
        else:
            answer = -1
    else:
        answer = -1
        
    return answer