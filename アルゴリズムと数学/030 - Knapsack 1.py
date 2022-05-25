N,W = map(int,input().split())
w,v = [0],[0]
dp = [[-1]*(W+1) for _ in range(N+1)]

for  i in range(N):
    wi,vi, = map(int,input().split())
    w.append(wi)
    v.append(vi)
    dp[i][0] = 0

for n in range(1,N+1):
    for weight in range(W+1):
        dp[n][weight] = dp[n-1][weight]
        if 0 <= weight-w[n] <= W and dp[n-1][weight-w[n]] >= 0:
            dp[n][weight] = max(dp[n][weight],dp[n-1][weight-w[n]]+v[n])

print(max(dp[N][:]))