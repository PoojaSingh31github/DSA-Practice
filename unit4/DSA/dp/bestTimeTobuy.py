def max_profit(n,arr):
  profit = 0
  for i in range(n-1):
    if arr[i] < arr[i+1]:
      profit += arr[i+1] - arr[i]
  return profit    


for _ in range(int(input())):
  n=int(input())
  arr = list(map(int,input().split()))
  ans = max_profit(n,arr)
  print(ans)