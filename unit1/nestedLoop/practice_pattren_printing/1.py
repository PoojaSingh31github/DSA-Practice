n=4
m=4
for i in range(n):
    for j in range(m):
        if i==0 or i==n-1 or j==0 or j==m-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")    
    print() 

for i in range(n):
    print(" "*i + "*"*m)
print()    

for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()    

for i in range(n-1,-1,-1):
    print(" "*i + "*"*(n-i)) 

for i in range(1,n):
    print(" "*i + "*"*(n-i))    
    
                
count=1                
for i in range(n):
    for j in range(i):
        print(count, end=" ")
        count+=1
    print()    

