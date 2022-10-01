from collections import deque

N,M = map(int,input().split())
used = [21e8] * 100001
result = []
def bfs(N,cnt):
    q = deque([(N,cnt)])

    while q:
        N,cnt = q.popleft()
        if 0 <= N < 100001:
            if cnt < used[N]:
                used[N] = cnt
            else:
                continue

            q.append([N-1,cnt+1])
            q.append([N+1,cnt+1])
            q.append([N*2,cnt])

bfs(N,0)
print(used[M])