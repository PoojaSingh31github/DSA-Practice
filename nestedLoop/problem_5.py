num = int(input("Enter the size of the diamond: "))
for i in range(1,num*2,1):
    for j in range(1,num*2,1):
        if  i + j == num + 1 or j - i == num - 1 or i - j == num - 1 or i + j == num * 3 - 1:
            print("*",end="")
        else:
            print(' ', end="")    
    print()   
        