
# Grand Pa problem 
for grandfather in range(4):
    for sam in range(4):
        print("Collected apple from row", grandfather , "column" , sam)



# Visualization 2
for i in "ABCDE":
    for j in "ABCDE" :
        print(i , j)
        

# Visualization 1
for family in range(1, 6 , 1):
    for gappas in range(1, 5, 1):
        print(family, "ate", gappas , "Gol gappa")


# print - 1
for i in range(1, 11):
    for j in range(1, 11):
        print("Father Count :" , i , ", son completed", j)


# Pattern Printing - 1
for i in range(1, 6):
    bag = ""
    for j in range(1, 11):
        bag = bag + "*" + " "
    print(bag)



# Pattern print - 2
for i in range(1,6):
    bag = ""
    for j in range(0 , i):
        bag = bag + "*" + " "
    print(bag)


# Pattern Printing - 3
for i in range(1, 6):
    bag = ""
    for j in range(1 , i+1):
        bag = bag + str(j) + " "
    
    print(bag)



# Pattern Printing - 4 
for i in range(6 , 1 , -1): 
    bag = ""
    for j in range(1 , i):
        bag = bag + "* "
    
    print(bag)


# Pattern printing - 5

for i in range(5 , 0 , -1):
    bag = ""
    for j in range(1 , i+1 ):
        bag = bag + str(j) + " " 
    print(bag)



# Pattern Printing - 6
for i in range(1 , 6 ):
    bag = ""
    for j in range(1 , i ):
        bag = bag + str(j) + " " 
    print(bag)


for i in range(5 , 0 , -1):
    bag = ""
    for j in range(1 , i+1 ):
        bag = bag + str(j) + " " 
    print(bag)



# Break 
for sultan in range(1 , 11):
    for bahubali in range(1,11):
        if sultan < bahubali :
            break
        print(sultan , bahubali)


# Continue 
for i in "ABCDE":
    for j in "ABCDE":
        if i == j :
            continue
        print(i , j)