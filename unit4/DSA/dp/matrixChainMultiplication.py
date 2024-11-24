A = [10, 20, 30, 40, 30]

n = len(A) - 1
dp = [[0 for _ in range(n)] for _ in range(n)]

for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')  

        for k in range(i, j):
            q = dp[i][k] + dp[k+1][j] + A[i] * A[k+1] * A[j+1]
            if q < dp[i][j]:
                dp[i][j] = q

print(dp[0][n-1]) 



