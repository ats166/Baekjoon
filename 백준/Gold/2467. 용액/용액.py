target = 21e8
N = int(input())
arr = list(sorted(map(int,input().split())))
start, end = 0, N-1

while end > start:
    tmp = arr[start] + arr[end]

    if abs(target) > abs(tmp):
        target = abs(tmp)
        a,b = arr[start],arr[end]
        if abs(arr[start]+arr[end-1]) > abs(tmp):
            start += 1
        else:
            end -= 1
    else:
        if abs(arr[start]+arr[end-1]) > abs(tmp):
            start += 1
        else:
            end -= 1

print(a,b)