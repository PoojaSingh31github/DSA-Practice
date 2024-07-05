h = int(input("Enter the  brick wall pattern of height: "))
w = int(input("Enter the  brick wall pattern of width: "))

for i in range(1,w+1,1):
    for j in range(1,h+2,1):
        if i%2==1:
            print(" ","[]",end="")    
        else:
            print("[]"," ",end="")    
    print()
    
        