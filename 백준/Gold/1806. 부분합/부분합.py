N, target = map(int,input().split())
arr = list(map(int,input().split()))
start = 0
end = start+1
answer = 100001

if arr[start] >= target or arr[-1] >= target:
    answer = 0
tmp = arr[start] + arr[end]

while True:

    if tmp >= target:
        if answer > end - start:
            answer = end - start
        tmp -= arr[start]
        if start + 1 == N - 1:
            break
        start += 1
    else:
        if end + 1 == N:
            if start + 1 == N - 1:
                break
            tmp -= arr[start]
            start += 1
        else:
            end += 1
            tmp += arr[end]

if answer == 100001:
    print(0)
else:
    print(answer+1)