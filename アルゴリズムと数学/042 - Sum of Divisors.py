N = int(input())
f = [0]*(N+1)
for i in range(1,N+1):
    ii = i
    while ii <= N:
        f[ii] += 1
        ii += i

ans = 0
for i in range(1,N+1):
    ans += i*f[i]
print(ans)