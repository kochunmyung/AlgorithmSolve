T = int(input())

for i in range(T):
    stack = []
    a = input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을 경우는 VPS가 될 수 없으므로 NO 출력
                print("NO")
                break
    else:       #break문을 만나지 않았을경우 ()가 맞게 있으므로 스택이 비어있음
        if not stack:
            print("YES")
        else:   #스택에 괄호가 들어있으면 NO
            print("NO")