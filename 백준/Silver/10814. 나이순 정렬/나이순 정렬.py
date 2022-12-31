import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    tmp = input().split()
    arr.append([int(tmp[0]),tmp[1]])

arr.sort(key=lambda x : x[0])

for i in arr:
    print(i[0], i[1])