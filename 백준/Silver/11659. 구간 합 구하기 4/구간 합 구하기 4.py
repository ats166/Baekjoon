import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
sum_arr = [0]
tmp = 0
for i in range(N):
    tmp += arr[i]
    sum_arr.append(tmp)

for i in range(M):
    a,b = map(int,input().split())
    print(sum_arr[b] - sum_arr[a-1])