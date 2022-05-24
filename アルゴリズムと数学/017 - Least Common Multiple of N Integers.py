def gcd(A,B):
    big = max(A,B)
    small = min(A,B)

    while small != 0:
        tmp = big%small
        big = max(tmp,small)
        small = min(tmp,small)
    return big

def lcm(A,B):
    return A*B/gcd(A,B)

N = int(input())
a = list(map(int,input().split()))
ans = int(lcm(a[0],a[1]))

for i in range(2,N):
    ans = int(lcm(a[i],ans))
print(ans)