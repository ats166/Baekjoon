N = int(input())
M = int(input())
if M > 0 :
    btn = list(map(int,input().split()))
else:
    btn = []

cur = abs(100-N)

for i in range(1000001):
    for j in list(map(int,str(i))):
        if j in btn:
            break
    else:
        cur = min(cur, abs(i - N) + len(str(i)))

print(cur)