import math

N,K = map(int,input().split())
V = list(map(int,input().split()))
ans = 0

for i in range(1,2**K):
    cnt = -1
    lcm = 1
    for j in range(K):
        if i&(1<<j):
            cnt *= -1
            lcm = (lcm*V[j])//math.gcd(lcm,V[j])
    ans += cnt*(N//lcm)
print(ans)