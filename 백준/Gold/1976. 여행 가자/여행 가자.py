import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
M = int(input())
arr = [-1] * 201

for i in range(len(arr)):
    arr[i] = i

def findboss(member):

    if arr[member] == member:
        return member

    tmp = findboss(arr[member])
    return tmp

def union(a,b):

    fa,fb = findboss(a),findboss(b)

    if fa == fb:
        return

    arr[fb] = fa
    return
for i in range(N):
    route = list(map(int,input().split()))

    for j in range(N):
        if route[j] == 1:
            union(i+1, j+1)

mess = list(map(int,input().split()))
tmp = []
for i in range(len(mess)):
    tmp.append(findboss(arr[mess[i]]))

if len(set(tmp)) == 1:
    print('YES')
else:
    print('NO')