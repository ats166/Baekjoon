N,M = map(int,input().split())
arr = list(map(int,input().split()))
tmp = 0

for i in range(M):
    tmp += arr[i]

mmax = tmp

for j in range(M,N):
    tmp += arr[j]
    tmp -= arr[j-M]

    if mmax < tmp:
        mmax = tmp

print(mmax)