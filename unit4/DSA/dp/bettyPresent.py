def minCoinsRecursive(coins, n, P):
    # Base cases
    if P == 0:
        return 0  # No coins are needed to make zero amount
    if P < 0:
        return float('inf')  # Impossible to make negative amount

    min_coins = float('inf')
    for i in range(n):
        res = minCoinsRecursive(coins, n, P - coins[i])
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)

    return min_coins

# Wrapper function to handle impossible case
def getMinCoinsRecursive(coins, P):
    result = minCoinsRecursive(coins, len(coins), P)
    return result if result != float('inf') else -1

# Example usage:
P = 11
coins = [1, 2, 5]
print(getMinCoinsRecursive(coins, P))  # Output should be the minimum number of coins


# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

def minCoinsMemoization(coins, n, P, memo):
    # Base cases
    if P == 0:
        return 0
    if P < 0:
        return float('inf')

    # Check if result is already computed
    if P in memo:
        return memo[P]

    min_coins = float('inf')
    for i in range(n):
        res = minCoinsMemoization(coins, n, P - coins[i], memo)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)

    memo[P] = min_coins
    return memo[P]

# Wrapper function to handle impossible case
def getMinCoinsMemoization(coins, P):
    memo = {}
    result = minCoinsMemoization(coins, len(coins), P, memo)
    return result if result != float('inf') else -1

# Example usage:
P = 11
coins = [1, 2, 5]
print(getMinCoinsMemoization(coins, P))


# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


def minCoinsTabulation(coins, P):
    # Initialize dp array with "infinity" for impossible solutions
    dp = [float('inf')] * (P + 1)
    dp[0] = 0  # Base case: No coins needed for zero amount

    # Iterate over all amounts from 1 to P
    for amount in range(1, P + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[P] if dp[P] != float('inf') else -1

# Example usage:
P = 11
coins = [1, 2, 5]
print(minCoinsTabulation(coins, P))
