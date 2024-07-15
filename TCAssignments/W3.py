#question is write the pyhton funtion for calculating the area of circle   


r=23
pi=22/7


# area of cicle==pi*r^2  ====1661.9
def calculateAreaOfCircle(radius, pi):
    area=pi*radius*radius
    return area

result=calculateAreaOfCircle(r, pi)

print(result)

# {'o', 's', 'm', 'i', 'n', 'z', 'e'}
string="zoomsessionmooz"
str=set(string)
print(str)

for i in range(len(string)):
    for j in range(i+1,len(string)+1):
        print(string[i:j])