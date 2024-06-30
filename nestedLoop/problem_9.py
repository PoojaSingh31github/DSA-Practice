num = int(input("Enter the size of the triangle: "))
for i in range(1,num+1,1):
    for j in range(1,num+1,1):
        if i==j or j==1 or i==num:
            print("*",end="")
        else:
            print(" ", end="")  
    print()







