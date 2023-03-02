from collections import deque

used = [0] * 100001

A,B,N,M = map(int,input().split())
q = deque([N])
while q:
    tmp = q.popleft()
    if tmp == M:
        result = used[tmp]
        break
    if tmp - 1 >= 0 and used[tmp - 1] == 0:
        used[tmp - 1] = used[tmp] + 1
        q.append(tmp - 1)
    if tmp + 1 <= 100000 and used[tmp + 1] == 0:
        used[tmp + 1] = used[tmp] + 1
        q.append(tmp + 1)
    if tmp - A >= 0 and used[tmp - A] == 0:
        used[tmp - A] = used[tmp] + 1
        q.append(tmp - A)
    if tmp - B >= 0 and used[tmp-B] == 0:
        used[tmp - B] = used[tmp] + 1
        q.append(tmp - B)
    if tmp + A <= 100000 and used[tmp + A] == 0:
        used[tmp + A] = used[tmp] + 1
        q.append(tmp + A)
    if tmp + B <= 100000 and used[tmp + B] == 0:
        used[tmp + B] = used[tmp] + 1
        q.append(tmp + B)
    if tmp * A <= 100000 and used[tmp * A] == 0:
        used[tmp * A] = used[tmp] + 1
        q.append(tmp * A)
    if tmp * B <= 100000 and used[tmp * B] == 0:
        used[tmp * B] = used[tmp] + 1
        q.append(tmp * B)


print(used[tmp])