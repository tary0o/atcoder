N = int(input())
A = [0]+ list(map(int,input().split()))
M = int(input())
sumA = [0]*(N)

for i in range(1,N):
    sumA[i] = sumA[i-1]+A[i]

beforeB = int(input())
ans = 0
for _ in range(M-1):
    B = int(input())
    ans += abs(sumA[beforeB-1]-sumA[B-1])
    beforeB = B
print(ans)