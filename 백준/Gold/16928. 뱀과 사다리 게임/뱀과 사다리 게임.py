import copy

N,M = map(int,input().split())
arr = [-1] * 101
tmp = [-1] * 101
arr[1] = 0
acc = [False] * 101
cnt,flag = 0,0

for _ in range(N):
    a,b = map(int,input().split())
    acc[a] = b

for _ in range(M):
    a,b = map(int,input().split())
    acc[a] = b

while True:
    if arr[100] != -1:
        print(cnt)
        break

    cnt += 1
    for j in range(101):
        if arr[j] == cnt-1:
            for i in range(1,7):
                if j+i > 100:
                    flag = 1
                    break
                if acc[j+i] == False:
                    tmp[j+i] = cnt
                else:
                    tmp[acc[j+i]] = cnt
        if flag == 1:
            break
    arr = copy.deepcopy(tmp)
    tmp = [-1] * 101