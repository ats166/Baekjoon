arr = []
now = 0
cnt = 0
N = int(input())

for i in range(N):
    st,ed = map(int,input().split())
    arr.append([st,ed])

arr = sorted(arr, key=lambda x: (x[1], x[0]))

for i in range(N):
    if now <= arr[i][0]:
        now = arr[i][1]
        cnt += 1
print(cnt)