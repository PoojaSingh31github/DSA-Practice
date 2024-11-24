#1. find sum of a+b = k
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

#2. find reverse of array by two pointer 
array=[3,5,8,5,9,2]
n=len(array)
i=0
j=n-1
while i<j:
    # array[i],array[j] = array[j],array[i]   #in pyhton
    temp=array[i]                             # in js
    array[i]=array[j]
    array[j]=temp
    i+=1
    j-=1
print(array)

#3. find triplet sum a+b+c=k
# brute force 
ar=[5,6,3,4,8,9,1]
n=len(ar)
c=10
con=False
for i in range(n-2):
    for j in range(n-1):
        for k in range(n):
            if ar[i]+ar[j]+ar[k]==c:
                con=True

print(con)
# two pinter 
flag=False
ar.sort()
for i in range(n-2):
    l,r=i+1,n-1
    while l<r:
        sum=ar[i]+ar[l]+ar[r]
        if sum==c:
            flag=True
            break
        elif sum<c:
            l+=1
        else:
            r-=1
print(flag)            

#4. merge two sorted array
a1=[2,4,6,8]
a2=[1,3,5,7,9]
n1=len(a1)
n2=len(a2)
ans=[]*(n1+n2)
# print(ans)
i,j,k=0,0,0
while i<n1 and j<n2:
    if a1[i]<a2[j]:
        ans.append(a1[i])
        i+=1
        k+=1
    else:
        ans.append(a2[j])
        j+=1
        k+=1
print(ans)            

#5. remove duplicate from sorted array
a=[2,2,3,4,4,5,6,66,77,8,9,9,1]
n=len(a)
j=0
for i in range(n-1):
    if a[i]!=a[i+1]:
        a[j]=a[i]
        j+=1
a[j]=a[n-1]
for k in range(j+1):
    print(a[k], end=" ")

#4 sum
def fourSum(nums,target):
    nums.sort()
    n=len(nums)
    arr=[]
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k,l= j+1,n-1
            while k<l:
                s=nums[i]+nums[j]+nums[k]+nums[l]
                if s==target:
                    arr.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1     
                elif s>target:
                    l-=1
                else:
                    k+=1
        return arr 


     

