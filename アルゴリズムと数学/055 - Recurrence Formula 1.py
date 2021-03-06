mod = int(1e9+7)

def multiply(A,B):
    C = [[],[]]
    C[0].append((A[0][0]*B[0][0]+A[0][1]*B[1][0])%mod)
    C[0].append((A[0][0]*B[0][1]+A[0][1]*B[1][1])%mod)
    C[1].append((A[1][0]*B[0][0]+A[1][1]*B[1][0])%mod)
    C[1].append((A[1][0]*B[0][1]+A[1][1]*B[1][1])%mod)

    return C

N = int(input())
A = [[2,1],[1,0]]
ans = [[1,0],[0,1]]
for i in range(60):
    if (N-2)&(1<<i):
        ans = multiply(A,ans)
    A = multiply(A,A)

print(sum(ans[0][:])%mod)