N = int(input())
A = list(map(int,input().split()))
A.sort()

def divisor(A,B):
    big = max(A,B)
    small = min(A,B)

    while small != 0:
        tmp = big%small
        big = max(tmp,small)
        small = min(tmp,small)
    return(big)

tmp = divisor(A[0],A[1])
for i in range(2,N):
    tmp = divisor(tmp,A[i])
print(tmp)