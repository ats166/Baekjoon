from collections import deque
import sys
input = sys.stdin.readline
q = deque([])

N = int(input())
for i in range(N):
    command = list(input().split())

    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        try:
            print(q.popleft())
        except:
            print('-1')
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q) == 0:
            print('1')
        else:
            print('0')
    elif command[0] == 'front':
        if len(q) >= 1:
            print(q[0])
        else:
            print('-1')
    elif command[0] == 'back':
        if len(q) >= 1:
            print(q[-1])
        else:
            print('-1')
