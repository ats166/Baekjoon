arr = []
maxlen = 0
for i in range(5):
    x = list(input())
    if len(x) > maxlen:
        maxlen = len(x)
    arr.append(x)

for j in range(maxlen+1):
    for i in range(5):
        try:
            print(arr[i][j],end='')
        except:
            continue