X,Y = map(int,input().split())

a = (2*Y-X)
b = (2*X-Y)

if (a%3==b%3==0) and 2*Y-X>=0 and 2*X-Y>=0:

    for i in range(1,X+1):
    bunbo *= i
    bunbo = bunbo%mod
    for i in range(1,Y+1):
        bunbo *= i
        bunbo = bunbo%mod
    for i in range(1,X+Y+1):
        bunsi *= i
        bunsi = bunsi%mod
