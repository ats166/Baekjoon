N = int(input())
bucket = [-1] * N
people = list(map(int, input().split()))

for i in range(N):
    cnt = 0 
    for j in range(N):
        if cnt == people[i] and bucket[j] == -1:
            bucket[j] = i+1
            break
        elif bucket[j] == -1:
            cnt += 1
print(*bucket)