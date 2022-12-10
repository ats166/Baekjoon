import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N,M = map(int,input().split())
arr = [-1] * (N+1)

for i in range(N+1):
    arr[i] = i

def findboss(member):

    if arr[member] == member:
        return member
    else:
        arr[member] = findboss(arr[member])
        return arr[member]

def union(a, b):

    fa, fb = findboss(a), findboss(b)

    if fa == fb:
        return
    else:
        arr[fb] = fa
        return


for i in range(M):
    flag,x,y = map(int,input().split())

    if flag == 0:
        union(x, y)
    else:
        if findboss(x) == findboss(y):
            print('YES')
        else:
            print('NO')