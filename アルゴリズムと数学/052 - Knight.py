mod = 1000000007

X,Y = map(int,input().split())
a = (2*Y-X)
b = (2*X-Y)

if (a%3==b%3==0) and 2*Y-X>=0 and 2*X-Y>=0:
    a //= 3
    b //= 3
    bunbo,bunsi = 1,1
    for i in range(1,a+1):
        bunbo *= i
        bunbo = bunbo%mod

    for i in range(a):
        bunsi *= (a+b-i)
        bunsi = bunsi%mod

    p = bunbo%mod
    div = 1
    for i in range(30):
        if (mod-2)&(1<<i):
            div = (div*p)%mod
        p = (p*p)%mod
    
    print((bunsi*div)%mod)
else:
    print(0)