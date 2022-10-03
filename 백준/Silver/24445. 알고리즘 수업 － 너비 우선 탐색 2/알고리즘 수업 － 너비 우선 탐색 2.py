from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())

arr =[[] for _ in range(N)]
used = [0] * N
for i in range(M):
    a,b = map(int,input().split())

    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

def bfs(now):
    cnt = 1
    q = deque([arr[now]])
    while q:
        queue = q.popleft()
        queue.sort(reverse=True)

        for i in queue:
            if used[i] == 0:
                cnt += 1
                used[i] = cnt
                q.append(arr[i])

used[R-1] = 1
bfs(R-1)
for i in range(N):
    print(used[i])