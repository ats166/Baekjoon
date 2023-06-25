def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == ')' and len(stack) == 0:
            answer = False
            break
        elif s[i] == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append('(')
    if answer and len(stack) >= 1:
        return False
    else:
        return answer