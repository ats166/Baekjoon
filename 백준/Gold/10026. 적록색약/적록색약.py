from collections import deque
import copy
N = int(input())
arr = [list(input()) for _ in range(N)]
acc = copy.deepcopy(arr)
area = 0
def bfs(y,x,tmp,blind):
    q = deque([(y,x)])

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        y,x = q.popleft()

        for k in range(4):
            dy = directy[k] + y
            dx = directx[k] + x

            if dy >= N or dy < 0 or dx >= N or dx < 0:
                continue
            if blind == 1 and (tmp == 'R' or tmp == 'G'):
                if arr[dy][dx] != 'B' and arr[dy][dx] != 0:
                    arr[dy][dx] = 0
                    q.append([dy,dx])

            elif arr[dy][dx] == tmp:
                arr[dy][dx] = 0
                q.append([dy,dx])

for j in range(N):
    for i in range(N):
        if arr[j][i] != 0:
            area += 1
            tmp = arr[j][i]
            bfs(j,i,tmp,0)

print(area)
area = 0
arr = acc
for j in range(N):
    for i in range(N):
        if arr[j][i] != 0:
            area += 1
            tmp = arr[j][i]
            bfs(j,i,tmp,1)
print(area)