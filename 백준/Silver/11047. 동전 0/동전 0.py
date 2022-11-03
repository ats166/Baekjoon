N,M = map(int,input().split())

coin = []
cnt = 0
for i in range(N):
    tmp = int(input())
    coin.append(tmp)

coin.sort(reverse=True)

for i in range(N):
    if coin[i] <= M:
        tmp = M // coin[i]
        cnt += tmp
        M = M - (tmp*coin[i])

print(cnt)
