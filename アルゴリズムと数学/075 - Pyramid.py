mod = int(1e9+7)

N = int(input())
A = list(map(int,input().split()))
ans = 0

fact = [1]*(N+1)
for i in range(1,N+1):
    fact[i] = (fact[i-1]*i)%mod

for i in range(N):
    bunsi = fact[N-1]
    bunbo = (fact[N-1-i]*fact[i])%mod

    p = bunbo
    div = 1
    for j in range(30):
        if (mod-2)&(1<<j):
            div = (div*p)%mod
        p = (p*p)%mod
    
    ans = (ans+A[i]*(bunsi*div))%mod
print(ans)