N = int(input())
A = list(map(int,input().split()))
M = max(A)
cntA = [0]*(2*10**5 +1)
ans = 0

for a in A:
    cntA[a] += 1

for j in range(1,M+1):
    for k in range(1,int((M/j)//1+1)):
        i = j*k
        if i%1 == 0 and cntA[i] > 0:
            ans += cntA[i]*cntA[j]*cntA[k]

print(ans)