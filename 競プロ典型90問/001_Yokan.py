N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))
A.append(0)
ok = 0
ng = L

while (ng-ok) > 1:
    check = (ng+ok)//2
    k = 0
    l = 0
    for i in range(len(A)):
        if i == len(A)-1:
            l += L-A[i-1]
        else:
            l += A[i]-A[i-1]

            if l >= check:
                l = 0
                k += 1
            if k > K:
                break

    if   k > K:
        ok = check
    elif k < K:
        ng = check
    elif l < check:
        ng = check
    else:
        ok = check
print(ok)