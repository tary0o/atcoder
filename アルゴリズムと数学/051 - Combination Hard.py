mod = 1000000007

X,Y = map(int,input().split())
bunsi,bunbo = 1,1

for i in range(1,X+1):
    bunbo *= i
    bunbo = bunbo%mod
for i in range(1,Y+1):
    bunbo *= i
    bunbo = bunbo%mod
for i in range(1,X+Y+1):
    bunsi *= i
    bunsi = bunsi%mod

div = 1
p = bunbo%mod
for i in range(30):
    if (mod-2)&(1<<i):
        div = (div*p)%mod
    p = (p*p)%mod

print((bunsi*div)%mod)