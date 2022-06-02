N,Q = map(int,input().split())
B = [0]*(N-1)

for _ in range(Q):
    L,R,X = map(int,input().split())
    if L != 1:
        B[L-2] -= X
    if R != N:
        B[R-1] += X

for b in B:
    if b>0:
        print('>',end='')
    elif b==0:
        print('=',end='')
    elif b<0:
        print('<',end='')