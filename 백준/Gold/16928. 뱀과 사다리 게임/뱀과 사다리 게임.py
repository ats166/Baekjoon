import copy

N,M = map(int,input().split())
arr = [-1] * 101
tmp = [-1] * 101
acc = [False] * 101
arr[1] = 0
cnt,flag = 0,0

for _ in range(N+M):
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
                    break
                if acc[j+i] == False:
                    tmp[j+i] = cnt
                else:
                    tmp[acc[j+i]] = cnt
                    
    arr = copy.deepcopy(tmp)
    tmp = [-1] * 101
