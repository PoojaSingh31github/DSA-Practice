def isPossible(arr, n, p, mid):
  painter = 1
  timeSum = 0
  for i in range(n):
    if timeSum + arr[i] <= mid:
      timeSum += arr[i]
    else:
      painter += 1
      if painter > p or arr[i] > mid:
        return False
      timeSum = arr[i]
  return True

def painterPartition(arr, n, p):
  s = 0
  total = sum(arr)
  e = total
  ans = -1
  while s <=e:
    mid = s+(e-s)//2
    if isPossible(arr, n, p, mid):
      ans = mid
      e = mid -1
    else:
      s = mid + 1
  return ans

t = int(input())
for i in range(t):
  n, p = map(int, input().split())
  arr = list(map(int, input().split()))
  res = painterPartition(arr, n, p)
  print(res)