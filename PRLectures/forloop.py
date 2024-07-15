# ------------------------- FOR String -----------------------------
# For loop iteration with string 
for item in "Masai":
    print(item)


# For loop iteration with string 
for item in "Motu and patlu":
    print(item) 

# --------------------------FOR Range ------------------------------
# range(start , end , step) = 1 - 9 
for item in range(1,10,1):
    print(item)


# 1 , 3 , 5 , 9 - But with 2 jumps 
for item in range(1,11,2):
    print(item)

# 2 , 4 , 6 , 8 - But with 2 jumps
for item in range(2,11,2):
    print(item)


# One arguments - end ---------------------------------------
# tart from 0 to n-1
for item in range(10):
    print(item)


# Two arguments - start , end -------------------------------
# 5 - 9 
for item in range(5 , 10):
    print(item)


# Print Hello 5 times ---------------------------------------
for item in range(5):
    print("Hello pablo")


for item in range(1 , 6 , 1):
    print("Hello pablo")

# start = 1 2 3 4 5 6 
# 1 < 6 - True - Hello Pablo 
# 2 < 6 - True - Hello Pablo 
# 3 < 6 - True - Hello Pablo 
# 4 < 6 - True - Hello Pablo 
# 5 < 6 - True - Hello Pablo 
# 6 < 6 - False - Loop break 


# Print 1 to 5 in a Horizontal manner (Concatenation) -----
bag = ""
for item in range(1 , 6 , 1):
    bag = bag + str(item) 
print(bag) 


# What if I wrote print inside for loop --------------------
bag = ""
for item in range(1 , 6 , 1):
    bag = bag + str(item) 
    print(bag) 

# Sum of all the numbers from 1 to 5 -------------------------
sum = 0
for item in range(1 , 6 , 1):
    sum = sum + item
print(sum)



# How to run a reverse loop ----------------------------------
for item in range(5 , 0 , -1):
    print(item)


# How to run a reverse loop horizontal ------------------------
bag = ""
for item in range(5 , 0 , -1):
    bag = bag + str(item)
print(bag)


# Factorial Calculation ----------------------------------------
# 1 = 1
# 2 = 1 * 2 = 2
# 3 = 1 * 2 * 3 = 6
# 4 = 1 * 2 * 3 * 4 = 24


num = 3

fact = 1
for item in range(1 , num + 1 , 1):
    fact = fact * item
print(fact)


# Calculate the sum of even numbers from 1 to 50 -----------------

# Break it 
# final_outcome = sum 
# Need number from 1 to 50 
# Only even number - Condition 

sum = 0
for item in range(1, 51 , 1):
    if item % 2 == 0:
        sum = sum + item
print(sum)



# ------------------------ BREAK ------------------------------------
# Break 
# Guest problem 
total_guest = 7

for item in range(1 , total_guest+1 , 1):
    if item == 4:
        break
    print("Guest : ", item)


# First number which is divisible by 3 between 50 - 70 
for item in range(50 , 71 , 1):
    if item % 3 == 0:
        print(item)
        break


# ------------------------ CONTINUE ------------------------------------
# skip guest 3 as he is sick 
# Total Guest 7
for item in range(1 , 8 , 1):
    if item == 3:
        continue
    print(item)


# Printing all the numbers which are not divisble by 3 or 5 from 1 to 50
for item in range(1 , 51 , 1):
    if item % 3 == 0 or item % 5 == 0:
        continue
    print(item)