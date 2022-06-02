N,Q = map(int,input().split())
A = [0]+list(map(int,input().split()))
B = [0]*(N+1)

for i in range(1,N+1):
    B[i] += B[i-1]+A[i]

ans = []
for _ in range(Q):
    L,R = map(int,input().split())
    ans.append(B[R]-B[L-1])

for a in ans:
    print(a)