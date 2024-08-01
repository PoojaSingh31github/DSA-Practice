N = int(input("Enter the size of the square: "))
for i in range(1,N+1,1):
    bag=""
    for j in range(1,N+1,1):
        if i>1 and i<N and j>1 and j<N:
            bag=bag+" " 
        else:
            bag=bag+"*"  
    print(bag)          


