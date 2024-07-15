

# Example 1
friend1_age = 21
friend2_age = 20
friend3_age = 25
friend4_age = 21
friend5_age = 20
friend6_age = 28
friend7_age = 24


# Example 2
item1_name = "apple"
item2_name = "orange"
item3_name = "lichi"
item4_name = "banana"
item5_name = "grape"
item6_name = "mango"
item7_name = "pineapple"
item8_name = "strawberry"



friends_age = [21 , 20 , 25 , 21, 20 , 28 , 24]
items_name = ["apple" , "orange" , "lichi" , "banana" , "grape" , "mango" , "pineapple" , "strawberry"]

# ------------------------creating list------------------------------------

todo = ["Morning scrum" , "DSA Session" , "csbt comm session" , "coding session"  , "Daily Standup"]
print(todo)


# Can contain multiple data types
evaluation_scores = [9 , 8 , 7.5 , 9.3]
print(evaluation_scores)


mylist = ["Hello" , 12 , True , 3.14]
print(mylist)



# ------------------------ACCESSING DATA-----------------------------------------
# Example - 1
names = ["Pablo" , "Chunnu" , "Munnu" , "Samosa"  ]

# 0 -> n-1
print(names[1])
print(names[0])
print(names[2])

# What if we write 4
print(names[4])


# Example - 2
list = [1 , "masai" , 3.41 , [1 , 2, 3] , False]
print(list[3])
print(list[3][1])



# ------------------------------EXTRACTING MORE THAN ONE DATA FROM LIST-----------

list = [1 , "masai" , 3.41 , [1 , 2, 3] , False]
print(list[0:3:1]) #0 , 1 , 2
print(list[1:3:1]) #1 , 2
print(list[0:4:2]) #0 , 2 


print(list[2:]) #strt from 2 till end 
print(list[:3]) #start from 0 till 3 (Excluding 3)



# ------------------------------Finding Length --------------------------------
# Want to create biriani 
names = ["Potato" , "Rice" , "Tomato" , "Masala"]

print(len(names))
print(names[len(names) -1]) # Last Index


# ------------------------------Operations on List : ADD ------------------------------

# Append
brands = []
brands.append("Apple")
brands.append("Oppo")
brands.append("Samsung")
brands.append("Redmi")
brands.append("Realme")
brands.append("One plus")

# Add to s specific position 
# brands.insert( index , elemet )
brands.insert(0 , "HTC")
brands.insert(3 , "Google Pixel")

print(brands)


# Add mango at index 1
first = ["apple", "banana", "cherry"]
first.insert(1, "mango")
print(first)


# Replace  
numbers = [1 , 2 , 3 , 4 , 5]
numbers[0] = 10
numbers[3] = -15
print(numbers)



# -------------------------Remove elements : pop------------------------

# Code 1
nums = [1 , 2 , 3 , 4 , 5]

nums.pop()
nums.pop()
nums.pop()

nums.append(10)

print(nums) # 1 , 2 , 10 




# Code 2
nums = [1 , 2 , 3 , 4 , 5]


for i in range(3):
    nums.pop()

nums.append(10)

print(nums)


# Code 3
nums = [1 , 2 , 3 , 4 , 5]

nums.pop(2) #Remove element from index 2

print(nums)



# Code 4
nums = [1 , 2 , 3 , 4 , 5]

nums.remove(3) #it will remove 3

print(nums)



# ----------------------------------LOOP WITH LIST ------------------------

# Example 1
# Print all the elements in a loop 
heros = ["bat-man" , "super-man" , "iron-man"]

# Way - 1

for i in range(len(heros)):
    print(heros[i])

# Way - 2

for item in heros:
    print(item)


# Reverse loop - 1

for i in range(len(heros)-1 , -1 , -1 ):
    print(heros[i])

# Reverse loop - 2
for item in reversed(heros):
    print(item)



# Example 2 print game
category = ["movie", "cartoon", "Show" , "funny"]
names = ["iron man" , "Doremon" , "Shark Tank" , "Mr.Bean" ]

for i in range(len(names)):
    print(category[i] ,"=" ,names[i])



# Example 3 - calculate sum and average 
scores = [99 , 87 , 77 , 95 , 92]

sum = 0
for i in range(len(scores)):
    sum = sum + scores[i] 

print("Sum:" , sum)
print("Average:" , int(sum/len(scores)))


# Example - 4 find max 
scores = [99 , 87 , 77 , 95 , 92]

max = scores[0]
for i in range(1 , len(scores)):
    if max < scores[i]:
        max = scores[i]

print(max)


# Print only even number from the a list 
numbers = [1 , 2 , 3 , 4 , 5]

for i in numbers:
    if i % 2 == 0:
        print(i)
    

for i in numbers:
    if i % 2 == 1:
        continue
    print(i)


for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])