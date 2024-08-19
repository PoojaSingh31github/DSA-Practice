# find the maximum sum of all subarray of size k
array=[1,2,3,4,3,4,6,8,9,5,10,12,14]
n=len(array)
k= 4 #size of subarray
# brute force
# maax_sum=0
# for i in range(n-k+1):
#     sum=0
#     for j in range(i-1,i+k-2):
#         sum+=array[j]
#         if sum>maax_sum:
#             maax_sum=sum
# print(maax_sum)

# sliding window
# s=0
# for i in range(k):
#     s=s+array[i]
# res=s
# for i in range(k,n):
#     s=s-array[i-k]+array[i]
#     res=max(res,s)
# print(res)    

#Longest substring with at least k repeating characters
#Subarrays Having Sum Less Than M

#Find the size of largest sub-string which doesn't contains any repeated characters in given string
head=0
map={}
res=0
for tail in range(n):
    key=array[tail]
    while key in map  and  map[key]>0:
        res=max(res,tail-head)
        map[array[head]] -= 1
        head+=1
    if key in map:
        map[key]+=1
    else:
        map[key]=1
    print(max(res,tail-head))                



#Find the Longest Substring which contains K distinct / Unique characters