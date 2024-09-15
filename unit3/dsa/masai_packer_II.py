def masaiPackers(arr, n, k):
  min_days = float("inf")
  max_days = 1
  memo = {}

  def moveTruck(w, days):   #-1
    nonlocal min_days, max_days
    
    if w == 0:
      min_days = min(min_days, days) # 0
      max_days = max(max_days, days) #1
      return
    
    if w < 0:
      return   
    
    if (w, days) in memo:
      return memo[(w, days)]
    
    for i in range(k):    # k=3 capacity
      moveTruck(w - arr[i], days + 1)      # 0-1  , 1
    
    memo[(w, days)] = True
  
  moveTruck(n, 0)
  
  if min_days == float('inf'):
    return -1
  else:
    return min_days, max_days

n, k = map(int, input().split())
arr = [1,2,3]

res = masaiPackers(arr, n, k)

if res == -1:
  print(res)
else:
  print(*res)