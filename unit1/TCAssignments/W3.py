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



array=[[1,2,3,4,7], [2,3,4,5,6], [3,4,5,6,7], [4,5,6,7,8], [1,2,3,4,5]] 
for i in range(len(array)):
    dommyarray=[]
    for j in range(len(array)):
        if i+j==len(array)-1 or i==j:
            dommyarray.append(array[i][j])
        else:
            dommyarray.append(" ")   

    print()  
    print(dommyarray)  
