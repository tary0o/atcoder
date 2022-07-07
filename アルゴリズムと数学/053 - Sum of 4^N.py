mod = 1000000007

N = int(input())

p = 4%mod
bunsi = 1
for i in range(60):
    if (N+1)&(1<<i):
        bunsi = (bunsi*p)%mod
    p = (p*p)%mod
bunsi -= 1

p = 3%mod
bunbo = 1
for i in range(30):
    if (mod-2)&(1<<i):
        bunbo = (bunbo*p)%mod
    p = (p*p)%mod

print((bunsi*bunbo)%mod)