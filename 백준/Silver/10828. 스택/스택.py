import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = list(input().split())
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print('-1')
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack):
            print('0')
        else:
            print('1')
    elif command[0] == 'top':
        try:
            print(stack[-1])
        except:
            print('-1')
