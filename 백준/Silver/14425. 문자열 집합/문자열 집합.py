import sys
input = sys.stdin.readline

N,M = map(int,input().split())
a,cnt = [],0
for i in range(N):
    tmp = input()
    a.append(tmp)
a = set(a)

for i in range(M):
    tmp = input()
    if tmp in a:
        cnt += 1
print(cnt)