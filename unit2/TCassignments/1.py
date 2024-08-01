# inclass assignment 
n=9
arr= [1, 8, 6, 2, 5, 4, 8, 3, 7]

m=0
for i in range(n):
    for j in range(i+1,n):
        h=min(arr[i],arr[j])
        w=j-i
        area= h*w
        # print(area)
        m=max(m, area)
print(m)        

# takehome assigment 
arr= [1 , 4 , 3, 2 , 5 , 7]  
k=9
n=6  
found=False
for i in range(n):
    sum=0
    for j in range(i+1,n):
        sub_arr=arr[i:j]
        for i in sub_arr:
            sum+=i
    # print(sum)        
    if sum==k:
        found=True 
if found:
    print(True)
else:
    print(False)
        
                   
        
                  
        
            
        
                                  
