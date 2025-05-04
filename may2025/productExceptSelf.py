# // Product of Array Except Self
arr =[1,4,3,2]
# // output = [24 , 6 , 8, 12]
left =1
output = [1]*len(arr)
for i in range(len(arr)):
    output[i] *= left
    left *=arr[i]

right =1
for i in range(len(arr)-1,-1,-1):
    output[i] *= right
    right *= arr[i]
print(output)    
    


