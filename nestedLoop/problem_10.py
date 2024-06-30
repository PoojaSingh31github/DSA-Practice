num = int(input("Enter the size of the pyramid: "))
for i in range(num,0,-1):
    for j in range(1,(num*2),1):
        if i==j or i<2 or j+i==num*2:
            print("*",end="")
        else:
            print(" ", end="")  
    print()