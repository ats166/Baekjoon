import sys
input = sys.stdin.readline

N = int(input())
arr = list(sorted(map(int,input().split())))
target = int(input())
cnt = 0
start, end = 0, N-1

while end > start:
    tmp = arr[start] + arr[end]

    if tmp > target:
        end -= 1
    else:
        start += 1
    if tmp == target:
        cnt += 1

print(cnt)