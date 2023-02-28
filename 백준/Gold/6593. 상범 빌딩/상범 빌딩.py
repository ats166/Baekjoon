import sys
from collections import deque
# input = sys.stdin.readline()

directZ = [0,0,0,0,1,-1]
directY = [-1,1,0,0,0,0]
directX = [0,0,-1,1,0,0]

while True:
    mat = []
    L, R, C = map(int,input().split())

    if L + R + C == 0:
        break

    for i in range(L):
        arr = []
        for j in range(R):
            tmp = list(input())
            arr.append(tmp)
        space = input()
        mat.append(arr)

    def bfs(z,y,x):
        q = deque([(z,y,x)])

        while q:
            zz,yy,xx = q.popleft()

            for k in range(6):
                dz = directZ[k] + zz
                dy = directY[k] + yy
                dx = directX[k] + xx

                if dy >= R or dy < 0 or dx >= C or dx < 0 or dz >= L or dz < 0:
                    continue
                if mat[dz][dy][dx] == 'E':
                    q = []
                    return mat[zz][yy][xx] + 1

                elif mat[dz][dy][dx] == '.':
                    q.append([dz,dy,dx])
                    mat[dz][dy][dx] = mat[zz][yy][xx] + 1





    flag = False
    for i in range(L):
        if flag:
            break
        for j in range(R):
            for k in range(C):
                if mat[i][j][k] == 'S':
                    mat[i][j][k] = 0
                    result = bfs(i,j,k)

    if result != None:
        print(f"Escaped in {result} minute(s). ")
    else:
        print('Trapped!')