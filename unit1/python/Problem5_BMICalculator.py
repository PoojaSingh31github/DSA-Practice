weigth= int(input("enter weight in kilograms "))
heigth= float(input("enter height in meters.") )
if heigth>0 and weigth>=0:
        BMI = weigth/(heigth * heigth)
        print(BMI)
else:
    if heigth>0.0:
        print("Invalid input, height cannot be zero.") 
    else:
        print("Invalid input, height and weight must be positive numbers.")           