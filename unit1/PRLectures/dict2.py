# ------------- METHODS IN DICT ----------------------
# items 
# get 
# keys 
# values 

classDetails = {
    "topic" : "Dictionary 2",
    "start_time" : "16:30",
    "end_time" : "18:00",
    "course_details" : {
        "batch" : "ft37",
        "course" : "pr104"
    },
    "zoom_link" : "https://zooom.in/12345678"
}


print(classDetails)

# keys ------------------------------------------------
print(classDetails.keys())


keys = classDetails.keys()
print(keys[0]) # Error 


keys = list(classDetails.keys())
print(keys[0])



# values --------------------------------------------
print(classDetails.values())


values = list(classDetails.values())
print(values)
print(values[3])


# get -----------------------------------------------

classDetails = {
    "topic" : "Dictionary 2",
    "start_time" : "16:30",
    "end_time" : "18:00",
    "course_details" : {
        "batch" : "ft37",
        "course" : "pr104"
    },
    "zoom_link" : "https://zooom.in/12345678"
}




# 1
print(classDetails.get("start_time"))

print(classDetails["start_time"])


# 2
print(classDetails.get("start")) # No Error - None 

print(classDetails["start"]) # Error



# 3
print(classDetails.get("start" , "Key is not present"))

print(classDetails.get("start" , False ))


# 4
if classDetails.get("start" , False):
    print("Start key is present")
else:
    print("Start key is not present")




# Items ----------------------------------------

classDetails = {
    "topic" : "Dictionary 2",
    "start_time" : "16:30",
    "end_time" : "18:00",
    "course_details" : {
        "batch" : "ft37",
        "course" : "pr104"
    },
    "zoom_link" : "https://zooom.in/12345678"
}




print(classDetails.items())

print(list(classDetails.items())) # List of Tuples 

list_of_tuples = list(classDetails.items())


# 2
list_of_tuples = list(classDetails.items())

for single_tuple in list_of_tuples:
    print(single_tuple[0] , single_tuple[1])


