N = int(input())
A = list(map(int,input().split()))
cnt = [0]*(2*10**5+1)

for a in A:
    cnt[a] += 1
dp = [[1,0,0,0] for _ in range(2*10**5+1)]

for i in range(1,2*10**5+1):
    dp[i][1] = dp[i-1][1]+dp[i-1][0]*cnt[i]
    dp[i][2] = dp[i-1][2]+dp[i-1][1]*cnt[i]
    dp[i][3] = dp[i-1][3]+dp[i-1][2]*cnt[i]
print(dp[2*10**5][3])