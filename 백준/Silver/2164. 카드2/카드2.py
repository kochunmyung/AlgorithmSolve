import sys
from collections import deque

N = int(sys.stdin.readline())
answer = deque()

for i in range(N):
  answer.append(i+1)

while True:
  if len(answer) == 1:
    print(answer.pop())
    break
  answer.popleft()
  a = answer.popleft()
  answer.append(a)
