def Count_with_cond(arr,k):
  def count_set(i,s):
    if i==len(arr):
      if s==k:
        return 1
      else:
        return 0
    e_count=count_set(i+1,s)
    i_count=count_set(i+1,s+arr[i])
    return e_count+i_count
  return count_set(0,0)   

n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=Count_with_cond(arr,k)
print(ans)
