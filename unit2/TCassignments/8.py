# # subarray substring
# array=[1,2,3,4,3,4,6,8,9,5,10,12,14]
#     # 0 1 2 3 4 5 6 
      
# n=len(array)
# k=4
# s=0
# for j in range(k):
#     s+=array[j]
# print(s)   
# max_sum=s
# for j in range(k,n):  #k=4  j=4  5 6 6 
#     s = s-array[j-k] + array[j]
#     if max_sum<s:
#         max_sum=s
# print(max_sum)



# #  s = s - array[j - k] + array[j] 

# step 1= 34 64 25.......
#         34 25 64 12.....
#         34 25 12 64 ......                     n-i-1
#         34 25 12  22 64 11 90 
#         34 25 12  22 11 64 90 
#         34 25 12  22 11 64 90 

# step 2  25 34 12 ......
#         25 12 34 22 11...
#         25 12 22 34 11...
#         25 12 22 11 34 64 90 
#         25 12 22 11 34 64 90   


array=[64, 34, 25, 12, 22, 11, 90]
n=len(array)
for i in range(n):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)            