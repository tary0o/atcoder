N = int(input())
A = sorted( list(map(int,input().split())) )
B = sorted( list(map(int,input().split())) )
C = sorted( list(map(int,input().split())) )

ans = 0
for b in B:
    if b<=A[0] or b>=C[N-1]:
        continue

    ok = 0
    ng = N
    while(ng-ok>1):
        mid = (ok+ng)//2
        if A[mid] < b:
            ok = mid
        else:
            ng = mid
    a = ok+1

    ok = N
    ng = -1
    while(ok-ng>1):
        mid = (ok+ng)//2
        if C[mid] > b:
            ok = mid
        else:
            ng = mid
    c = N-ok

    ans += (a*c)
print(ans)