def max_profit(n, l, prices):
    dp = [0] * (l + 1)
    for length in range(1, l + 1):
        for j in range(n):
            rod_length = j + 1 
            if rod_length <= length:
                dp[length] = max(dp[length], dp[length - rod_length] + prices[j])
                
    return dp[l]
n, l = map(int, input().split())
prices = list(map(int, input().split()))
print(max_profit(n,l,prices))
