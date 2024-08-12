# spriral  technique
num=int(input())
for i in range(num):
  n,m=map(int,input().split())
  arr=[]
  for j in range(n):
    arr.append(list(map(int,input().split())))
    left, right, top ,bottom = 0,m-1,0,n-1
  count=0
  total=n*m
  while left <= right and top <= bottom:
    for i in range(bottom,top-1,-1):
      if count<total:
        print(arr[i][left],end=" ")
        count+=1
    left+=1
    
    for j in range(left,right+1): # right=3  ight=4
      if count<total:
        print(arr[top][j],end=" ")
        count+=1
    top+=1
    
    for i in range(top,bottom+1): #2   3
      if count<total:
        print(arr[i][right],end=" ")
        count+=1
    right-=1
    
    for j in range(right,left-1,-1):
      if count<total:
        print(arr[bottom][j],end=" ")
        count+=1
    bottom-=1  
  print()  
    