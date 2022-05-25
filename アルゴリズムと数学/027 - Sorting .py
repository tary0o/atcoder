N = int(input())
A = list(map(int,input().split()))

def merge(l,r):
    C = []
    if l-r == 1:
        C.append(min(A[l],A[r]))
        C.append(max(A[l],A[r]))
        return C
    elif l==r:
        C.append(A[l])
        return C
    
    m = (l+r)//2
    C1 = merge(l,m)
    C2 = merge(m+1,r)
    cntC1 = 0
    cntC2 = 0

    for _ in range(r-l+1):
        if cntC1==len(C1):
            C.append(C2[cntC2])
            cntC2 += 1
        elif cntC2==len(C2):
            C.append(C1[cntC1])
            cntC1 += 1
        else:
            if C1[cntC1] >= C2[cntC2]:
                C.append(C2[cntC2])
                cntC2 += 1
            else:
                C.append(C1[cntC1])
                cntC1 += 1
    return C

A = merge(0,N-1)
print(*A)