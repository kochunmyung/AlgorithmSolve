N, M = map(int,input().split())
card=list(map(int,input().split()))

card.sort()

for _ in range(M):
    x = card[0] + card[1]
    card[0]=card[1]=x
    card.sort()

print(sum(card))