N,A,B = map(int,input().split())
SUM = 0

for i in range(N+1):
    I = str(i)
    length = len(I)
    sum = 0
    for l in range(length):
        sum += int(I[l])

    if A <= sum <= B:
        SUM += i

print(SUM)