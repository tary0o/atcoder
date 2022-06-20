N = int(input())
X = list(map(int,input().split()))

ans = 1e10

for i in range(1,101):
    tmpans = 0
    for j in range(N):
        tmpans += (X[j]-i)**2
    ans = min(ans,tmpans)
print(ans)