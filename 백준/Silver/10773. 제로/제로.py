import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    tmp = int(input())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)

print(sum(stack))