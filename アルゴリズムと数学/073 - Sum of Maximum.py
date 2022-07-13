mod = 1000000007

N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)

ruijou = [1]*N
for i in range(1,N):
    ruijou[i] = (ruijou[i-1]*2)%mod
ans = 0
for i in range(N):
    ans = (ans + A[i]*ruijou[N-i-1])%mod
print(ans)