Principal = int(input("enter principle amount ")) 
Rate =int(input("enter the rate of interest per year ")) 
Time = int(input("enter the time in years. ")) 
z =Principal*Rate*Time/100
if Principal>=0 and Rate>=0 and Time>=0:
    print(z)
else:
    print("Invalid input, all values must be non-negative.")    
    