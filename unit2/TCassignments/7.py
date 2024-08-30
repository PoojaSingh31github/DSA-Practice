array =[3,5,8,2,6,9]          # 12  9
target= 7
n=len(array)

# a+b=taget       

# for i in range(n):
#     for j in range(i+1,n):
#         s=array[i]+array[j]
#         if s==target:
#             print(i, "=",array[i],j,"=",array[j])
#             break

# array =[3,5,8,2,6,9]             #2 3 5 6 8 9   6 9 
i=0
j=n-1
flag=False
array.sort()
while i<j:
    s=array[i]+array[j]
    print(i,j)
    if s==target:
        print(array[i],array[j])
       
        flag=True
        i+=1
        j-=1
        break
    elif s>target:
        j-=1
    else:
        i+=1    
print(flag)




