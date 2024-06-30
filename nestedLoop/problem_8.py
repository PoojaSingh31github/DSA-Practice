num = int(input("Enter the size of the pyramid: "))
for i in range(1,num+1,1):
    for j in range(num,0,-1):
        if i+j>num+1:
            print(" ",end="")
        else:
            print(j,end="")    
    print()    
        