t = int(input()) 
test_cases = [int(input()) for _ in range(t)]
max_n = 113  
dp = [float('inf')] * (max_n + 1)
dp[0] = 0

for i in range(1, max_n + 1):
    if i >= 10:
        dp[i] = min(dp[i], dp[i - 10] + 1)
    if i >= 12:
        dp[i] = min(dp[i], dp[i - 12] + 1)

results = []
for n in test_cases:
    if dp[n] == float('inf'):
        results.append(-1)
    else:
        results.append(dp[n])

print(results)


