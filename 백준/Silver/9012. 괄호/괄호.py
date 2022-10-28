N = int(input())

for i in range(N):
    arr = list(input())
    stack = []
    flag = 0
    for j in range(len(arr)):
        if arr[j] == '(':
            stack.append(arr[j])
        elif arr[j] == ')':
            if '(' in stack:
                stack.pop()
            else:
                flag = 1
                break
    if flag == 1 or len(stack) >= 1:
        print('NO')
    else:
        print('YES')