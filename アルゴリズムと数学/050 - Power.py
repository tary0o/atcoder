a,b = map(int,input().split())
mod = 1000000007
ans = 1
p = a%mod

for i in range(30):
    if b&(1<<i):
        ans = (ans*p)%mod
    p = (p*p)%mod
print(ans)