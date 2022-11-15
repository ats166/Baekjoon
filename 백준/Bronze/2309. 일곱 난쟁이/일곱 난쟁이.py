lst = []
for i in range(9):

    a = int(input())
    lst.append(a)

for i in range(1<<9):
    sum_lst = []
    for j in range(9):
        if i & (1 << j):
            sum_lst.append(lst[j])
    if sum(sum_lst) == 100 and len(sum_lst) == 7:
        sum_lst.sort()
        print(*sum_lst)
        break