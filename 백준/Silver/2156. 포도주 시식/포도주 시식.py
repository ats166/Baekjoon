import sys
input = sys.stdin.readline

N = int(input())
arr = []
dp = [0] * N
for i in range(N):
    arr.append(int(input()))

dp[0] = arr[0]

if N >= 2:
    dp[1] = arr[0] + arr[1]
if N >= 3:
    for i in range(2,N):
        dp[i] = max(max((dp[i-3] + arr[i-1] + arr[i]),(dp[i-2] + arr[i])), dp[i-1])

print(dp[-1])