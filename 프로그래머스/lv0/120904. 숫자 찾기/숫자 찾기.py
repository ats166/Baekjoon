def solution(num, k):
    num = str(num)
    idx = -1
    
    for i in range(len(num)):
        print(num[i])
        if int(num[i]) == k:
            idx = i+1
            break;
    return idx