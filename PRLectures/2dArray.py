# row , col , position of sam & dada
# Idea of matrix - 4*4 

# -------------NESTED LOOP-----------
for i in range(4):  
    for j in range(4):
        print(i , j)



# 00 - a1r1
# 01 - a2r1
# 02 - a3r1
# 03 - a4r1
# 10 - a1r2
# 11 - a2r2
# 12 - a3r2
# 13 - 
#  so on...


# -------- ARRAY INSIDE AN ARRAY -----

filed = [
    ["a1" , "a2" , "a3" , "a4"],
    ["a1" , "a2" , "a3" , "a4"],
    ["a1" , "a2" , "a3" , "a4"],
    ["a1" , "a2" , "a3" , "a4"]
]

# list of list - MULTI DIMENTIONAL LIST 
print(filed)
print(filed[0])
print(filed[2][0])
# print(filed[4])
# print(field[i][j])


# Is this index position looking like same
# what we saw in sam dada ji example ?


# Are you able to relate ut with sam and dada ji example ?


# Running loop in matrix -------------------

filed = [
    ["a1f1" , "a2f1" , "a3f1" , "a4f1"],
    ["a1f2" , "a2f2" , "a3f2" , "a4f2"],
    ["a1f2" , "a2f2" , "a3f2" , "a4f2"],
    ["a1f2" , "a2f2" , "a3f2" , "a4f2"]
]

# list of list - MULTI DIMENTIONAL LIST 

for i in range(4):
    bag = ""
    for j in range(4):
        bag = bag + filed[i][j] + " "

    print(bag)




# Create one more multi dimentional list ---

list = [
    [1 , 2 , 3],
    [4, 5, 6],
    [7 , 8 , 9]
]


for i in range(3):
    for j in range(3):
        print(list[i][j], end=" ")

# Idea of Row - col 
for i in range(len(list)):
    for j in range(len(list[0])):
        print(list[i][j])



# print proper way 
for i in range(len(list)):
    bag = ""
    for j in range(len(list[0])):
        bag = bag + str(list[i][j]) + " "
    print(bag)



# sum all the element in a row
for i in range(len(list)):
    sum = 0
    for j in range(len(list[0])):
        sum = sum + list[i][j]
    print(sum)





# sum of index -----------------
list = [
    [1 , 2],
    [3 , 4],
    [5, 6]
]

# (0,0) (0,1)
# (1,0) (1,1)
# (2,0) (2,1)


# Sum of index will be 
# 0 1
# 1 2
# 2 3


for i in range(len(list)):
    bag = ""
    for j in range(len(list[0])):
        bag = bag  + str(i+j) + " "
    print(bag)





# Even sum in rows --------------
list = [
    [1 , 2 ,3],
    [4 , 5 ,6 ],
    [7 , 8 , 9]
]

# 2
# 10
# 8


for i in range(len(list)):
    sum = 0
    for j in range(len(list[0])):
        if list[i][j] % 2 == 0:
            sum = sum + list[i][j]
    print(sum)




# Go in Zig Zag --------------------------

list = [
    [1 , 2, 3, 4 ,5],
    [6 , 7 , 8 , 9 , 1],
    [3 , 2 , 5 , 4 , 6],
    [7, 8, 9, 1, 2]
]

# if dada is odd sam will run normal
# if dada is even sam will run reverse

for i in range(len(list)):
    bag = ""
    if i % 2 == 0:
        for j in range(len(list[0]) -1 , -1 , -1 ):
            bag = bag + str(list[i][j]) + " "

    else:
        for j in range(len(list[0])):
            bag = bag + str(list[i][j]) + " "

    print(bag)





# Traverce in any diraction with tricks

list = [ 
    [1 , 8 , 9],
    [2 , 7 , 10],
    [3 , 6 , 11],
    [4 , 5 , 12]
]


# Trick 
# (i,j)
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
# (3,0) (3,1) (3,2)


# Fix - 2 - j 
# Changing - i 

# j will be in outer loop - 2 , 0 
# i will be in inner loop - 0 , 3 


for j in range(len(list[0])-1 , -1 , -1):
    bag = ""
    for i in range(len(list)):
        bag = bag + str(list[i][j]) + " "
    print(bag)

