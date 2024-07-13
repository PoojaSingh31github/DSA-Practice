# Feature	
# Syntax	
# Ordered	 
# Mutable	 
# Duplicates	
# Example	

list=[1,2,3,4,5, "apple","orange"]
set={1,2,3,4,5,1,2,3,4,5}
tuple=(1,2,3,4,5,2,3,4,2,3,5)
dic={
    "first_name":"pooja",
    "last_name":"singh",
    "age":23,
    "hobbies":["cricket","coding"]
}

# list.append("heyyy")
# set.add(34)
# tuple.count(2)
# print(tuple.count(2))

set.pop()
print(set)

# dic["class"]="Xth"
# dic.pop("class")
# print(dic)
# print(dic.pop())

#question :- write a pyhton program for calculating the count of vowel in string

string="apple"
count=0
for i in range(len(string)):
    if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
        count+=1
print(count)   


    

