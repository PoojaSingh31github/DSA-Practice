def reach(N, X, jumps):
    dp = [False] * (X + 1)
    dp[0] = True  
    for i in range(N):
        a, b = jumps[i]
        new_dp = dp[:]
        for j in range(X + 1):
            if dp[j]: 
                if j + a <= X:
                    new_dp[j + a] = True  # `a` distance ka jump
                if j + b <= X:
                    new_dp[j + b] = True  # `b` distance ka jump
        dp = new_dp
    return "Yes" if dp[X] else "No"

# Example usage
N = 2
X = 10
jumps = [(3, 6), (4, 5)]
print(reach(N, X, jumps))  
