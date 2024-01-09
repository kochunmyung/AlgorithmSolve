while(True):
    word = input()

    # 스택이 비어있으면 yes로 하도록 설계
    stack = []

    if word == '.':
        break

    for i in word: # 왼쪽방향괄호는 무조건 균형잡인 시작점이므로 스택에 추가부터 해야함
        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ')':
            if len(stack) !=0 and stack[-1] == '(':   #반복문을 돌다가 오른쪽방향 괄호를 만나게되면 스택이 비어있으면 무조건 불균형이므로 스택에 추가하고 반복문탈출
                stack.pop()
            else:
                stack.append(i)
                break
        elif i ==']':
            if len(stack) !=0 and stack[-1] =='[':
                stack.pop()
            else:
                stack.append(i)
                break




    if len(stack)==0:
        print('yes')
    
    else:
        print('no')
         