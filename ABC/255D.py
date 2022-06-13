N,Q = map(int,input().split())
A = [0] +list(map(int,input().split()))
A.sort()
ans = []
sumA = [A[0]]

for i in range(1,N+1):
    sumA.append(sumA[i-1]+A[i])

for _ in range(Q):
    X = int(input())
    ok = 0
    ng = N+1
    while ng-ok>1:
        chk = (ok+ng)//2
        if A[chk]==X:
            ok = chk
            break
        elif A[chk]<X:
            ok = chk
        elif A[chk]>X:
            ng = chk
    
    B = -2*sumA[ok]+sumA[N]+(ok)*X-(N-ok)*X 
    ans.append(B)

for a in ans:
    print(a)