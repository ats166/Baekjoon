from collections import deque

def solution(maps):
    answer = 0
    
    q = deque([(0,0)])
    maps[0][0] = 101
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    while q:
        y,x = q.popleft()
        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x
            
            if dy >= len(maps) or dy < 0 or dx >= len(maps[0]) or dx < 0:
                continue
            if maps[dy][dx] == 1:
                maps[dy][dx] = maps[y][x] + 1
                q.append([dy,dx])
    

    if maps[-1][-1] == 1:
        return -1
    else:
        return (maps[-1][-1]-100)