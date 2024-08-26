n=int(input())
for i in range(n):
  a=int(input())
  array=list(map(int,input().split()))
  arr = [[0] * a for _ in range(a)]
  r=len(arr)
  c=len(arr[0])
  
  left, right,top,bottom = 0, c-1,0,r-1
  count=0
  total=r*c
  while count<total:
    for j in range(left,right+1,1):
      if count<total:
        arr[top][j] = array[count]
        count+=1
    top+=1
    for i in range(top,bottom+1,1):
      if count<total:
        arr[i][right]= array[count] 
        count+=1
    right-=1
    for j in range(right,left-1,-1):  # -1
      if count<total:
        arr[bottom][j]=array[count] 
        count+=1 
    bottom-=1    
    for i in range(bottom,top-1,-1):
      if count<total:
        arr[i][left]=array[count]  
        count+=1
    left+=1  
  # print(arr)
  sum=0
  for i in range(r):
    for j in range(c):
      if i==j or i+j== r-1:
        sum+=arr[i][j]
  print(sum)      
  
 