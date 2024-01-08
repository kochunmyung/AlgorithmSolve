n = int(input())

for _ in range(n):
    left = []
    right = []
    command = input()

    for i in command:
        # 입력 값이 < 인 경우 왼쪽 리스트의 마지막 문자를 오른쪽으로 보내줌 빈 리스트일 경우 아무일도 일어나지 않는다
        if i == '<':
            if left:
                right.append(left.pop())
        
        # 입력 값이 > 인 경우 오른쪽 리스트의 마지막 문자를 왼쪽 리스트로 보내줌 빈 리스트일 경우 아무일도 일어나지 않는다
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

        # 오른쪽 리스트의 순서가 반대로 정렬 되기 때문에 reversed이용해서 리스트를 뒤집어준다음 왼쪽리스트와 합친다
    left.extend(reversed(right))
    print(''.join(left))