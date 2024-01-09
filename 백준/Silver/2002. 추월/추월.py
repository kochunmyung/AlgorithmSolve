N = int(input())

incar = {}
outcar = {}

for k in range(N):
    number = input()
    incar[k] = number

for k in range(N):
    number = input()
    outcar[number] = k

count = 0

for i in range(1,N):
    for j in range(0, i):
        if outcar[incar[j]] > outcar[incar[i]]:
            count += 1
            break

print(count)

