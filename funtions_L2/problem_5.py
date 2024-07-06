def calculateFactorial(n):
    mul=1
    for i in range(1, n+1):
        mul*=i
    print("result =",mul)    

calculateFactorial(5)