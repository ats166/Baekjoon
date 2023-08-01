import sys
input = sys.stdin.readline

TC = int(input())

for tc in range(TC):

    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(list(map(int,input().split())))

    a = sorted(arr)
    top = 0
    cnt = 1

    for j in range(1,N):
        if a[j][1] < a[top][1]:
            top = j
            cnt += 1

    print(cnt)