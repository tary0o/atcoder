N = int(input())
A = list(map(int,input().split()))
arr = [ []*(N+1) for _ in range(N+1)]
anser = []

for i in range(1,N+1):
    arr[A[i-1]].append(i)
Q = int(input())

for _ in range(Q):
    L,R,X = map(int,input().split())
    if len(arr[X]) == 0:
        ans = 0
    elif L > arr[X][-1] or R < arr[X][0]:
        ans = 0
    elif len(arr[X]) == 1:
        if L <= arr[X][0] <= R:
            ans = 1
        else:
            ans = 0
    else:
        ok = 0
        ng = len(arr[X])
        while ng-ok>1:
            check = (ok+ng)//2
            if arr[X][check] <= R:
                ok = check
            else:
                ng = check
        indexR = ok
        
        ok = len(arr[X])-1
        ng = -1
        while ok-ng>1:
            check = (ok+ng)//2
            if arr[X][check]>= L:
                ok = check
            else:
                ng = check
        indexL = ok
        ans = indexR - indexL + 1
    
    anser.append(ans)

for a in anser:
    print(a)