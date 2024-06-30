num =int(input("Enter the size of the diamond: "))
for i in range(1,num+1,1):
    for j in range(1,i+1,1):
        print("*", end="")
    print()    
for i in range(num,0,-1):
    for j in range(1,i,1):
        print("*", end="")
    print()      

