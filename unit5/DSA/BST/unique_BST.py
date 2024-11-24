MOD = 10**9 + 7

def count_unique_bsts(T, test_cases):
  # Precompute dp array for all N up to 2000
  max_n = 2000
  dp = [0] * (max_n + 1)
  dp[0] = 1  # Base case: 1 BST with 0 nodes (empty tree)
  
  for n in range(1, max_n + 1):
    dp[n] = 0
    for root in range(1, n + 1):
      dp[n] += dp[root - 1] * dp[n - root]
      dp[n] %= MOD  # Take modulo to avoid overflow
  
  # Process each test case
  results = []
  for n in test_cases:
    results.append(dp[n])
  return results

# Input handling
T = int(input())  # Number of test cases
test_cases = []
for _ in range(T):
  test_cases.append(int(input()))

# Output results
results = count_unique_bsts(T, test_cases)
for res in results:
  print(res)
