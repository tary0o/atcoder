import copy
N,S = map(int,input().split())
A = [0]+list(map(int,input().split()))

dp = [[-1]*(S+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1,N+1):
    for j in range(S+1):
        dp[i][j] = dp[i-1][j]
        if 0 <= j-A[i] <= S and dp[i-1][j-A[i]]>=0:
            dp[i][j] = 1

for i in range(N+1):
    if dp[i][S] == 1:
        print('Yes')
        exit()
print('No')