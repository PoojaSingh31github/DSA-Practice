def pracel_count(array,k):
  n=len(array)
  array.sort()
  l=0
  r=n-1
  
  count=0
  while l<=r:
    s = array[l]+array[r]
    if s<=k:              # 4  3   4
      l+=1
      
    r-=1                   #2   
    count+=1
  print(count)  

k=3
array=[1,2,2,3]           #12  3   2
pracel_count(array,k)       
