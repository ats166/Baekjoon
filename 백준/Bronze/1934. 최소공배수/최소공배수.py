import copy
N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    A = copy.deepcopy(a)
    B = copy.deepcopy(b)
    while True:
        if a < b:
            a += A
        elif a > b:
            b += B
        elif a==b:
            print(a)
            break