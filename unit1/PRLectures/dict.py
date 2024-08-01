

# -------------------------Basics and How to create ----------
# List 
l = ["Chunnu" , "Laal" , 23 , True , ["Cricket" , "Coding" ]]

# 0 , 1 , 2, 3, 4
# first_name , last_name , age , is_student , hobbies 


# Dict - Example 1
userDetails = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23 ,
    "is_student" : True , 
    "hobbies" : ["Cricket" , "Coding"] 
}

print(userDetails)


# Dict with number as a key 
userDetails = {
    1: "Chunnu",
    2 : "Laal",
    3 : 23 ,
    4 : True , 
    5 : ["Cricket" , "Coding"] 
}


# Dict - Example 2

productDetail = {
    "name" : "Macbook Air",
    "brand" : "Apple",
    "price" : 95000,
    "category" : "Electronics",
    "specification" : {
        "ram" : 8,
        "processor" : "m1",
        "display" : "apple ratina",
        "storage" : 256
    }
}


student = {
    "name": "Rahul",
    "age": 23,
    "location": "Nainital",
    "age" : 26,
    "is_married" : False,
    "highest_degree" : "Btech"
}

# Dict is ordered and when you add the existing key it will modify the value of it
# Duplicate values will overwrite existing values:
print(student)
print(type(student))



# Example of nested dictionaries
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])  # Output: Alice



# -------------Accessing Elements ---------------------

userDetails = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23 ,
    "is_student" : True , 
    "hobbies" : ["Cricket" , "Coding"] 
}

# dictName["key Name"] --------------------------

print(userDetails["age"]) # 23
print(userDetails["hobbies"]) #["Cricket" , "Coding"] 
print(userDetails["hobbies"][1]) # Coding 
print(len(userDetails["hobbies"])) # 2


# When key is not present we will get Key Error ------
print(userDetails["city"])



# Writting conditional statement -------------------
if userDetails["is_student"] == True:
    print("I am a Masai Student and working on my skill to get high salary")
else:
    print("I got placed by Masai")



# Loop through a dict ---------------------------
for key in userDetails:
    print(key ,":" , userDetails[key])



# Length ----------------------------
print(len(userDetails))



# Removing Dict Element -------------------------------

userDetails = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23 ,
    "is_student" : True , 
    "hobbies" : ["Cricket" , "Coding"] 
}


# How to remove a key from dict 
# Removing using pop 
userDetails.pop("age")
print(userDetails)


# You can also use
del userDetails["age"]


# Remove the last one
userDetails.popitem()


# Remove all the keys 
userDetails.clear()
print(userDetails)


# ----------------ADD NEW ITEMS ----------------
userDetails = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23 ,
    "is_student" : True , 
    "hobbies" : ["Cricket" , "Coding"] 
}


userDetails["city"] = "Bangalore"
print(userDetails)






# ----------------UPDATING ELEMENTS -------------
# - If the key is already present, then the existing value gets updated.
# - If the key is not present, a new (**key: value**) pair is added to the dictionary.
# Dict are mutable - that means you can modify it 

userDetails = {
    "first_name" : "Chunnu",
    "last_name" : "Laal",
    "age" : 23 ,
    "is_student" : True , 
    "hobbies" : ["Cricket" , "Coding"] 
}

userDetails["age"] = 27

print(userDetails)


# Check if a key is present or not -------------------
print("name" in userDetails)
print("first_name" in userDetails)

