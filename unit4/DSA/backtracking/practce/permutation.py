def permutation(n,arr,start,curr):
   if start == n:
      curr.append(arr.copy())
      return 
   for i in range(start,n):
      arr[start],arr[i] == arr[i], arr[start]
      permutation(n,arr,start+1,curr)
      arr[start],arr[i] == arr[i], arr[start]


n=3
a=[1,2,3]
ans = permutation(n,a,0,[])
print(a)

