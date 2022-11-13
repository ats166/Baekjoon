N = int(input())
arr = sorted(map(int,input().split()))
time = 0

for i in range(N):
    time += arr[i]*N
    N -= 1

print(time)