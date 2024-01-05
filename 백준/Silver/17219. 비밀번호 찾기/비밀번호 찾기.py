import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dicti = {}

for _ in range(N):
    site, pwd = input().split()
    dicti[site] = pwd
    
for _ in range(M):
    print(dicti[input().rstrip()])