n=5
dp= [-1]*(n+1)

dp[0] = dp[1] = dp[2] = 1
dp[3] = 2

for i in range(4,n+1):
    dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
print(dp[n])