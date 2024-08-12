# find sum of a+b = k
arr=[9,0,3]
n=len(arr)
k=11 #a+b=k

def find_sum(arr,n,k):
    arr.sort()
    i,j=0,n-1
    while i<j:
        if arr[i]+arr[j]==k:
            return True
        if arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1 
    return False           


answer=find_sum(arr,n,k)
print(answer)
    

