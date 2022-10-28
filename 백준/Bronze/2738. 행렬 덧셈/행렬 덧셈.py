N,M = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(N)]
arr2 = [list(map(int,input().split())) for _ in range(N)]
result = [[0]*M for _ in range(N)]

for j in range(N):
    for i in range(M):
        result[j][i] = arr[j][i]+arr2[j][i]

for i in range(N):
    print(*result[i])