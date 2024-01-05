N = int(input())
array = set(map(int,input().split()))
M = int(input())
x = list(map(int,input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')