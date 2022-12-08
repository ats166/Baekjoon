import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M,N = map(int, input().split())
edge = []

for _ in range(N):
    tmp1,tmp2 = map(int,input().split())
    edge.append([tmp1,tmp2])

arr = [-1] * 500001

def findboss (member):
    if arr[member] == -1:
        return member

    tmp = findboss(arr[member])

    return tmp

def union(a,b):

    fa, fb = findboss(a), findboss(b)

    if fa == fb:
        return 1
    else:
        arr[fb] = fa

answer = 0
for i in range(N):
    a, b = edge[i]
    result = union(a, b)
    if result == 1:
        answer = i+1
        break

if answer:
    print(answer)
else:
    print(answer)