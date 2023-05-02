from heapq import heappop,heappush
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    n = int(input())

    if n == 0:
        if len(arr) == 0:
            print(0)
            continue
        tmp = heappop(arr)[1]
        print(tmp)

    else:
        heappush(arr,(-n, n))