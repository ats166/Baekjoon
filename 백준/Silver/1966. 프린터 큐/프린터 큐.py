tc = int(input())

for i in range(tc):
    N,target = map(int,input().split())
    important = list(map(int,input().split()))
    cnt = 0
    flag = False

    while True:
        if flag:
            break
        mmax = max(important)

        for j in range(N):
            if important[j] == mmax:
                cnt += 1
                if j == target:
                    print(cnt)
                    flag = True
                    break
                important[j] = 0
                mmax = max(important)