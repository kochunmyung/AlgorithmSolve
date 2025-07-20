def solution(s):
    stack = []
    answer = True
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0