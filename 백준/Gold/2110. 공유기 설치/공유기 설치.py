import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(sorted(int(input()) for _ in range(N)))
start, end = 1, arr[-1]-arr[0]
result = 0

while end >= start:
    mid = (start + end) // 2
    current = arr[0]
    cnt = 1

    for i in range(N):
        if arr[i] >= current + mid:
            cnt += 1
            current = arr[i]

    if cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)