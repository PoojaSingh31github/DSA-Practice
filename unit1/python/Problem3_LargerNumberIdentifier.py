# here i took 2 value and conpare then which one is larger and if both are eqaul or not.
num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
if num1> num2:
    print(num1 , "is larger than", num2)
elif num2 > num1:
    print(num2 , "is larger than", num1)
elif num1==num2:
    print("Both numbers are equal")    
        