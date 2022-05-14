mod = 998244353
N = int(input())
digits = len(str(N))

ans = 0
for i in range(digits-1):
    ans += ((1 + 9*10**i)*(10**(i+1)-10**i)//2)
    ans %= mod
ans += ((1 + N-10**(digits-1) + 1) * (N-10**(digits-1) + 1)//2)
ans %= mod

print(ans)