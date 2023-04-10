avg = 0
all = 0

for i in range(20):
    sub = list(input().split())
    tmp = 0.00
    if sub[-1] == 'A+':
        tmp = float(sub[1]) * 4.5
        all += float(sub[1])
    if sub[-1] == 'A0':
        tmp = float(sub[1]) * 4.0
        all += float(sub[1])
    if sub[-1] == 'B+':
        tmp = float(sub[1]) * 3.5
        all += float(sub[1])
    if sub[-1] == 'B0':
        tmp = float(sub[1]) * 3.0
        all += float(sub[1])
    if sub[-1] == 'C+':
        tmp = float(sub[1]) * 2.5
        all += float(sub[1])
    if sub[-1] == 'C0':
        tmp = float(sub[1]) * 2.0
        all += float(sub[1])
    if sub[-1] == 'D+':
        tmp = float(sub[1]) * 1.5
        all += float(sub[1])
    if sub[-1] == 'D0':
        tmp = float(sub[1]) * 1.0
        all += float(sub[1])
    if sub[-1] == 'F':
        tmp = 0
        all += float(sub[1])
    avg += tmp

if all == 0:
    print('0.000000')
else:
    print(round(avg/all,6))