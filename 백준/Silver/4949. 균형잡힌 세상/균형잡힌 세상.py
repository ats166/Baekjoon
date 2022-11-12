while True:
    data = input()
    if data[0] == '.':
        break
    else:
        stack = []
        flag = True
        for i in range(len(data)):
            if data[i] == '(':
                stack.append(data[i])
            elif data[i] == '[':
                stack.append(data[i])
            elif data[i] == ')':
                if stack == []:
                    flag = False
                    break
                elif stack[-1] != '(':
                    flag = False
                    break
                else:
                    stack.pop()
            elif data[i] == ']':
                if stack == []:
                    flag = False
                    break
                if stack[-1] != '[':
                    flag = False
                    break
                else:
                    stack.pop()
        # print(stack)
        if stack != [] or flag == False:
            print('no')
        elif stack == []:
            print('yes')