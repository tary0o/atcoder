N = int(input())
ans = 0
i = 0
cnt = 0
while i < N**2:
    i += 2*cnt+1
    for j in range(1,int(i**0.5)+1):
        if j**2==i:
            ans += 1
        elif i%j==0 and i/j <= N:
            ans += 2
    cnt += 1
print(ans)
