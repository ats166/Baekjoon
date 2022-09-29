from collections import deque

N,M = map(int,input().split())
q = deque([(N,0)])
used = [0] * 200000

def bfs():
    while q:
        n,c = q.popleft()

        if 0 <= n <= 100000:
            if used[n] == 0:
                used[n] += 1
            else:
                continue
            if n == M:
                print(c)
                break
            q.append([n-1,c+1])
            q.append([n+1,c+1])
            q.append([n*2,c+1])

bfs()