D,K = map(int,input().split())

bucket = [0] * D
first = 1
flag = False

for j in range(1,K):
    if flag:
        break
    for i in range(j+1,K):
        if flag:
            break
        bucket[0],bucket[1] = j,i
        for k in range(2,D):
            bucket[k] = bucket[k-1] + bucket[k-2]
            if bucket[-1] == K:
                flag = True
                break

print(bucket[0])
print(bucket[1])