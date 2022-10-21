import sys
input = sys.stdin.readline

N = int(input())
bucket = [0] * 10001

for i in range(N):
    a = int(input())
    bucket[a] += 1

for i in range(10001):
    if bucket[i] != 0:
        for j in range(bucket[i]):
            print(i)