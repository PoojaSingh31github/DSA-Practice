n,k = 5,2
arr = [10,20,30,40,30]

dp=[float("inf")]*n
dp[0]=0

for i in range(n):
  for j in range(i+1, min(i+k+1, n)):
    dp[j] = min(dp[j], dp[i]+abs(arr[i]-arr[j]))
    
print(dp)


