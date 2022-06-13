X,A,D,N = map(int,input().split())
Z = A+D*(N-1)

if D >= 0:
    if X <= A:
        print(A-X)
    elif X >= Z:
        print(X-Z)
    else:
        dn = X-A
        if dn%D == 0:
            print(0)
        elif dn%D <= D/2:
            if  X-dn%D>=A:
                print(dn%D)
            else:
                print(X-A)
        else:
            if X+dn%D<=Z:
                print(D-dn%D)
            else:
                print(Z-X)
else:
    if X >= A:
        print(X-A)
    elif X <= Z:
        print(Z-X)
    else:
        dn = X-A
        if dn%D == 0:
            print(0)
        elif dn%D <= D/2:
            if  X+dn%D>=Z:
                print(abs(D-dn%D))
            else:
                print(X-Z)
        else:
            if X-dn%D<=A:
                print(abs(dn%D))
            else:
                print(A-X)