arr = [list(map(int,input().split())) for _ in range(9)]
mmax = -21e8

for j in range(9):
    for i in range(9):
        if arr[j][i] > mmax:
            mmax = arr[j][i]
            y,x = j,i

print(mmax)
print(f'{y+1} {x+1}')