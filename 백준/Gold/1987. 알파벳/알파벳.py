
import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

N,M = map(int,input().split())

used = [0] * 101

arr = [list(input()) for _ in range(N)]

directy = [-1,1,0,0]
directx = [0,0,-1,1]
result = []
mmax = 0
def dfs(y,x,level):
    global mmax

    if level > mmax:
        mmax = level
        result.append(mmax)
    # print(level)
    for k in range(4):
        dy = directy[k] + y
        dx = directx[k] + x

        if dy >= N or dy < 0 or dx >= M or dx < 0:
            continue
        if used[ord(arr[dy][dx])] == 0:
            used[ord(arr[dy][dx])] = 1
            dfs(dy,dx,level+1)
            used[ord(arr[dy][dx])] = 0


used[ord(arr[0][0])] = 1
dfs(0,0,1)
print(max(result))