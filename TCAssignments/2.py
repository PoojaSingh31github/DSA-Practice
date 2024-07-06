# Write a program to find the maximum and minimum value in an array of integers.
set1={1,2,3,4,5,6,7,8,9} 

tuple=(2,3,457,8,9,0,0,98765,)
li=list(tuple)
# print(min(li))
# print(max(li))

minimum=li[0]
maximam=li[0]
for i in li:
    if maximam<i:
        maximam=i
    if minimum>i:
        minimum=i

print("maximam:",maximam)  
print("minimum:", minimum)      





