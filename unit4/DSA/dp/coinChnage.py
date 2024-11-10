arr = [1,2,3,5,6]
amt = 10
n=len(arr)
dp = [float('inf')]*(amt+1)

dp[0] = 0 # Base case: 0 coins are needed to make amount 0

for i in range(1,amt+1):
    for j in range(n):
        if i-arr[j] < 0:
            continue
        dp[i] = min(dp[i], 1 + dp[i-arr[j]])
if dp[amt] != float('inf'):
    print(dp[amt])
else:
    print(-1)            