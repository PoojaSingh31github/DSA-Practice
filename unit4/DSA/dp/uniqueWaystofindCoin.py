def countWaysRecursive(denominations, m, n):
    # Base cases
    if n == 0:
        return 1  # One way to make zero amount (by choosing no coins)
    if n < 0:
        return 0  # No solution if amount becomes negative
    if m <= 0 and n > 0:
        return 0  # No coins left and amount is still positive

    # Recursive case: include current coin or exclude it
    return countWaysRecursive(denominations, m - 1, n) + countWaysRecursive(denominations, m, n - denominations[m - 1])

# Example usage:
n = 4
denominations = [1, 2, 3]
m = len(denominations)
print(countWaysRecursive(denominations, m, n))

def countWaysMemoization(denominations, m, n, memo):
    # Base cases
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n > 0:
        return 0
    
    # Check if result is already computed
    if (m, n) in memo:
        return memo[(m, n)]

    # Recursive case with memoization
    memo[(m, n)] = countWaysMemoization(denominations, m - 1, n, memo) + countWaysMemoization(denominations, m, n - denominations[m - 1], memo)
    return memo[(m, n)]

# Example usage:
n = 4
denominations = [1, 2, 3]
m = len(denominations)
memo = {}
print(countWaysMemoization(denominations, m, n, memo))

def countWaysTabulation(denominations, m, n):
    # Create a dp array to store results of subproblems
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: One way to make amount 0

    # Update the dp array for all denominations
    for coin in denominations:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]

# Example usage:
n = 4
denominations = [1, 2, 3]
m = len(denominations)
print(countWaysTabulation(denominations, m, n))
