import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

arr = [[] for _ in range(N+1)]
used = [False] * (N+1)
result = [1] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)

def dfs(V):
    used[V] = True
    for i in arr[V]:
        if used[i] == False:
            result[i] = V
            dfs(i)

dfs(1)

for i in range(2,len(result)):
    print(result[i])