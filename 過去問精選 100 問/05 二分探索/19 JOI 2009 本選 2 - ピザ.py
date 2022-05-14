l = int(input())
n = int(input())
m = int(input())
d = [0] + sorted( [int(input()) for _ in range(n-1)] ) + [l]
k = [int(input()) for _ in range(m)]

ans = 0

for i in k:
    ok = -1
    ng = len(d)

    while ng-ok>1:
        mid = (ok+ng)//2
        if d[mid] > i:
            ng = mid
        else:
            ok = mid
    ans += min( abs(d[ok]-i), abs(d[ok+1]-i) )

print(ans)