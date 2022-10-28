N = int(input())
result = [[0] * 100 for _ in range(100)]
cnt = 0

for i in range(N):
    y,x = map(int,input().split())

    for j in range(10):
        for i in range(10):
            result[y+j][x+i] += 1

for j in range(100):
    for i in range(100):
        if result[j][i] >= 1:
            cnt += 1

print(cnt)