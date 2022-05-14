N = int(input())

dp = [[],[0,1,1,1,1,1,1,1,1,1,0]]

for i in range(2,N+1):
    dp.append([0,0,0,0,0,0,0,0,0,0,0])

    for j in range(1,10):
        dp[i][j] += (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1])%998244353

print(sum(dp[N])%998244353)