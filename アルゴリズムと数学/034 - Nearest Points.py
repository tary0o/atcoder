N = int(input())
x,y = [],[]
for _ in range(N):
    xi,yi = map(int,input().split())
    x.append(xi)
    y.append(yi)

ans = 10**60
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        dist = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
        ans = min(ans,dist)
print(ans)