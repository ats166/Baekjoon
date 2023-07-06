N = int(input())
arr = [['*'] * N for _ in range(N)]
cnt = N // 3

for j in range(cnt):
    idx = [i for i in range(N) if (i // 3 ** j) % 3 == 1]

    for k in idx:
        for l in idx:
            arr[l][k] = " "

print('\n'.join([''.join([str(i) for i in row]) for row in arr]))