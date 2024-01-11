v = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
word = input().split()

#알파벳 순으로 정렬
word.sort() 


def check(arr):
    # 자음과 모음 개수 0개로 설정
    v_count, c_count = 0, 0

    for i in arr:
        if i in v:
            v_count += 1  # 모음이면 모음개수 추가
        else:
            c_count += 1  # 자음개수추가
    
    if v_count >=1 and c_count >=2: #
        return True
    else:
        return False

def backtracking(arr): # 탈출 조건으로 암호 리스트의 길이가 L이되면 check 함수를 통해 모음 자음 확인 참이면 암호 출력 후 리턴 길이가 아직 L이 아닌경우엔 알파벳하나씩 추가하고 backtracking 재귀호출
    if len(arr) == L:
        if check(arr):
            print("".join(arr))
            return
    
    for i in range(len(arr), C):
        if(arr[-1] < word[i]):
            arr.append(word[i])
            backtracking(arr)
            arr.pop()

for i in range(C-L+1):   # 알파벳을 시작으로 backtracking 함수 호출 암호문의 길이 L을 만들 수 없는 알파벳은 제외
    a = [word[i]] 
    backtracking(a)

