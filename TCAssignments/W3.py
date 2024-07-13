#question is write the pyhton funtion for calculating the area of circle   


r=23
pi=22/7


# area of cicle==pi*r^2  ====1661.9
def calculateAreaOfCircle(radius, pi):
    area=pi*radius*radius
    return area

result=calculateAreaOfCircle(r, pi)

print(result)


