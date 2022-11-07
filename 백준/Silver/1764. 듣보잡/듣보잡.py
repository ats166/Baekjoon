import sys

N,M = map(int,input().split())

listen = set()
watch = set()

for i in range(N):
    tmp = str(sys.stdin.readline().strip())
    listen.add(tmp)

for i in range(M):
    tmp = str(sys.stdin.readline().strip())
    watch.add(tmp)

result = sorted(list(listen & watch))

print(len(result))
for res in result:
    print(res)