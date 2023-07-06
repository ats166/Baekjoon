N = int(input())
arr = []
cnt = 0

def hanoi(N,start,end,helper):
    global cnt

    if N == 1:
        arr.append(start)
        arr.append(end)
        cnt += 1
        return

    hanoi(N-1,start,helper,end)
    arr.append(start)
    arr.append(end)
    cnt += 1
    hanoi(N-1,helper,end,start)

hanoi(N,1,3,2)
print(cnt)
for i in range(0,len(arr),2):
    print(f'{arr[i]} {arr[i+1]}')