def hanoi(N, start, end, helper):
    global cnt
    global new_list
    if N == 1:
        new_list.append(start)
        new_list.append(end)
        cnt += 1
        return
    hanoi(N-1, start, helper, end)
    new_list.append(start)
    new_list.append(end)
    cnt +=1
    hanoi(N-1, helper, end, start)

new_list = []
cnt = 0
hanoi(int(input()),1,3,2)

print(cnt)
for i in range(0,len(new_list),2):
    print (f'{new_list[i]} {new_list[i+1]}')