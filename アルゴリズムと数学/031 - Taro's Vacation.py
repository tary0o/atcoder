N = int(input())
A = [0]+list(map(int,input().split()))

dp = [[[] for _ in range(2)] for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = 0

for i in range(1,N+1):
    # i日目に勉強した場合
    dp[i][1] = dp[i-1][0] + A[i]

    # i日目に勉強しない場合
    dp[i][0] = max(dp[i-1][0],dp[i-1][1])
print(max(dp[N]))