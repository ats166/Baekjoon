N = int(input())
A = list(map(int,input().split()))
M = int(input())
targets = list(map(int,input().split()))
A.sort()

for target in targets:
    start = 0
    end = N - 1

    while True:
        mid = (start+end) // 2
        if target == A[mid]:
            print(1)
            break

        if target < A[mid]:
            end = mid - 1
        elif target > A[mid]:
            start = mid + 1
        
        if start > end:
            print(0)
            break