arr = input().split('-')
N = 0

for i in arr[0].split('+'):
    N += int(i)
    
for i in arr[1:]:
    for j in i.split('+'):
        N -= int(j)

print(N)