def merge_conquer(arr,l,mid,r):
  n1=mid-l+1
  n2=r-mid
  L=[0]*n1
  R=[0]*n2
  for i in range(n1):
    L[i]=arr[l+i]
  for i in range(n2):
    R[i]=arr[mid+1+i]
  i,j=0,0
  k=l
  while  i<n1 and j<n2:
    if L[i]<=R[j]:
      arr[k]=L[i]
      i+=1 
    else:
      arr[k]=R[j] 
      j+=1
    k+=1  
  while i<n1:
    arr[k]=L[i]
    i+=1
    k+=1
  while j<n2:
    arr[k]=R[j]
    j+=1
    k+=1 

def merge_divide(arr,l,r):
  if l<r:
    mid=l+(r-l)//2
    merge_divide(arr,l,mid)
    merge_divide(arr,mid+1,r)
    merge_conquer(arr,l,mid,r)

arr=[38,72,43,9,3,82,10]
n=7
ans=merge_divide(arr,0,n-1)
print(arr)