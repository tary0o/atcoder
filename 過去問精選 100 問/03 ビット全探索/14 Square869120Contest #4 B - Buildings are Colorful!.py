N,K = map(int,input().split())
a = list( map(int,input().split()) )

ans = 10**23
for i in range(2**(N-1)):
    bit = [ i>>j&1 for j in range(N-1) ]

    cnt = 1
    cost = 0
    height = a[0]
    for j in range(N-1):
        if bit[j] == 1:
            cost += max(height+1 - a[j+1],0)
            height = max(height+1,a[j+1])
            cnt += 1
        else:
            if height < a[j+1]:
                height = a[j+1]
                cnt += 1

    if cnt >= K:
        ans = min(ans,cost)

print(ans)