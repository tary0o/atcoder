N = int(input())
abc = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        a1,b1,c1 = abc[i]
        a2,b2,c2 = abc[j]
        if a1/b1==a2/b2:
            continue
        x = (c1*b2-c2*b1)/(a1*b2-a2*b1)
        y = (c1*a2-c2*a1)/(b1*a2-b2*a1)

        for k in range(N):
            a,b,c = abc[k]
            if not a*x+b*y<=c:
                break
        else:
            ans = max(x+y,ans)
print(ans)