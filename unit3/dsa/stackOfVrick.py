def stack_brick(arr1,arr2,n,x,y):
  res = 0
  arr1.sort()
  arr2.sort()
  for i in range(n):
    if arr1[i] == arr2[i]:
      continue
    
    elif arr1[i] < arr2[i]:
      diff = arr2[i] - arr1[i]
      res += diff * x
      
    elif arr1[i] >  arr2[i]:
      diff = arr1[i] - arr2[i]
      res += diff * y
      
  return res          

# for _ in range(int(input("enter tc "))):
#   n=int(input())
#   x=int(input())
#   y=int(input())
#   arr1=[]
#   arr2=[]
#   for i in range(n):
#     n,m=map(int,input().split())
#     arr1.append(n)
#     arr2.append(m)
  
print(stack_brick([3,1,1],[1,2,2],3,6,4))

#   1
# 3
# 6
# 4
# 3 1
# 1 2
# 1 2
    