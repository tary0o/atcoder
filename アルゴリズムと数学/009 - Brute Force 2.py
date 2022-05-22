import copy
N,S = map(int,input().split())
A = [0]+list(map(int,input().split()))

dp = [[[0]*(N+1) for _ in range(S+1)] for _ in range(N+1)]

for i in range(1,N+1):
    if A[i] <= S:
        dp[1][A[i]][0] = 1
        dp[1][A[i]][i] = 1

for i in range(1,N):
    for j in range(1,S+1):
        for k in range(1,N+1):
            if dp[i][j][0]==1 and dp[i][j][k]!=1 and j+A[k]<=S :
                dp[i+1][j+A[k]] = copy.copy(dp[i][j])
                dp[i+1][j+A[k]][k] = 1

for i in range(1,N+1):
    if dp[i][S][0] == 1:
        print('Yes')
        exit()
print('No')