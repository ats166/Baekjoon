from collections import deque

N = int(input())
arr = deque([])
for i in range(1,N+1):
    arr.append(i)

for i in range(N):
    if len(arr) == 1:
        print(arr[0])
        break
    tmp = arr.popleft()
    tmp = arr.popleft()
    arr.append(tmp)