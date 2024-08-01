def  calDistance(x1,y1,x2,y2):
    d1= x1-x2
    d2= y1-y2
    return (d1**2 + d2**2)**.5

x1, y1 = 2, 3
x2, y2 = 5, 7

distance=calDistance(x1,y1,x2,y2)
print(distance)