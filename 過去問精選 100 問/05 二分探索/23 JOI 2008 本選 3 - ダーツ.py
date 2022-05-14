import bisect

N,M = map(int,input().split())
P = [0] + [int(input()) for _ in range(N)]
S = set()

for i in range(N):
    for j in range(N):
        if P[i] + P[j] <= M:
            S.add(P[i] + P[j])

P = sorted(S)

ans = 0
for i in range(len(P)):
    x = M-P[i]
    ok = bisect.bisect(P,x)
    ans = max(ans,P[i]+P[ok-1])
    """
    ok = 0
    ng = len(P)
    while(ng-ok>1):
        mid = (ok+ng)//2

        if P[mid] <= x:
            ok = mid
        else:
            ng = mid
    ans = max(ans,P[i]+P[ok])
    """


print(ans)