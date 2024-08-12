# arr=[
#      [1,2,3,10,12],
#      [4,5,6,23,25],
#      [7,8,9,45,56]
#      ]
# r=len(arr)
# c=len(arr[0])

# left, right,top,bottom = 0, c-1,0,r-1
# count=0
# total=r*c
# while count<total:
#     for j in range(left,right+1,1):
#         if count<total:
#             print(arr[top][j],end=' ')
#             count+=1
#     top+=1
#     for i in range(top,bottom+1,1):
#         if count<total:
#             print(arr[i][right], end=" ")  
#             count+=1
#     right-=1
#     for j in range(right,left-1,-1):  # -1
#         if count<total:
#             print(arr[bottom][j],end=" ")  
#             count+=1 
#     bottom-=1    
#     for i in range(bottom,top-1,-1):
#         if count<total:
#             print(arr[i][left],end=" ")  
#             count+=1
#     left+=1     

n=37
sum=0
numbers=str(n)
for i in numbers:
    
    sum+=(int(i)**3)
# print(sum)    
if sum==n:
    print("true")
else:
    print("false")    
    

