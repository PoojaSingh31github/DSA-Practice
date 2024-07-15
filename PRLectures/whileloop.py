
# -----------------INCREMENT & DECREMENT -----------------
# Increment by 1
x = 10
x = x+1

# Or - x += 1
print(x)

# Increment by 5
y = 5
y = y+5

# Or - y += 5
print(y)


# Decrement by 1
x = 10
x = x-1

# Or - x -= 1
print(x)


# Increment by 5
y = 5
y = y-5

# Or - y -= 5
print(y)


# Activity 1
x=10
x+=1
x=x+5
x=x+10
print(x)   # 26
x-=10
x=x-5
print(x);   # 11


# Activity 2
a=10
c=a+1
b=10
d=b+1
print(a) # 10
print(b) # 10
print(c) # 11
print(d) # 11


# ----------------- WHILE LOOP ---------------------------
print("Hello Pablo")


# Way 1
print("Hello Pablo")
print("Hello Pablo")
print("Hello Pablo")
print("Hello Pablo")
print("Hello Pablo")

# ----------------------------------------------------------

# Loop Condition :
#     print("Hello Pablo")

# Conditionn - Run This 5 Times

# -----------------------------------------------------------

start = 0
while start < 5 :
    print("Hello Paablo")
    start = start + 1


# start = 0 1 2 3 4 5
# 0 < 5 - True 
# 1 < 5 - True 
# 2 < 5 - True
# 3 < 5 - True
# 4 < 5 - True 
# 5 < 5 - False 



# Output 
# print("Hello Paablo")
# print("Hello Paablo")
# print("Hello Paablo")
# print("Hello Paablo")
# print("Hello Paablo")

# ----------------------------------------------------------

start = 0
while start < 5 :
    print("Hello Paablo")
    # start = start + 1 -> Infinite Loop 

# start = 0 
# 0 < 5 - True 
# 0 < 5 - True 
# 0 < 5 - True 
# 0 < 5 - True 
# 0 < 5 - True 
# so on..


# Output 
# print("Hello Pablo")
# print("Hello Pablo")
# print("Hello Pablo")
# print("Hello Pablo")
# print("Hello Pablo")
# print("Hello Pablo")
# So on ...



# -----------------------------------------------
# How to create an infinite loop 

# while True:
#     print("I will run forever...")


# -----------------------------------------------



#  Print numbers from 1 to 5
start = 0
while start < 5:
    print(start+1)
    start = start + 1


# Print numbers from 1 to 15 
start = 0
while start < 15:
    print(start+1)
    start = start + 1



# If I increment by 2 then what will happen?
start = 0
while start < 15:
    print(start+1)
    start = start + 2

# 3 Jump 

# 5 Jump 



# Start with other numbers , print number from 100 to 150
start = 100
while start <= 150:
    print(start)
    start=start+1

# We can print 5 times like this also ----------------
start = 1
while start <= 5:
    print("Hello Pablo")
    start = start + 1



# Print numbers from 100 to 1 -----------------------
start = 100
while start >= 1:
    print(start)
    start = start - 1

# Send notice to 50 emp ------------------------------
emp_code = 1

while(emp_code <= 50):
    print("Notice sent to emp code : ", emp_code)
    emp_code = emp_code + 1


# Print odd numbers from 0 till given limit ----------
# 10 -> 1 3 5 7 9
start = 0
limit = 10
while start <= limit:
    if start % 2 == 1 :
        print(start)
    start = start + 1


# Print sum of all numbers from 1 - 10 ------------------
start = 1 
end = 3 
sum = 0

# 1 + 2 + 3 - 6

while start <= end :
    sum = sum + start
    print(sum)
    start = start + 1

print("Final Sum" , sum)

# Count even number from 1 to 10 ---------------------------
start = 1
end = 10
count = 0

while start <= end:
    if start % 2 == 0:
        count += 1
    start += 1

print(count)



# Print sum of all multiple of 3 from 0 to given limit ---
start = 0
limit = 10

# 3 , 6 , 9 -> 18

sum = 0
while start <= limit:
    if start % 3 == 0:
        sum = sum + start
    start = start + 1

print(sum)


# Print average of even number from 1 to 100 ---------------
# Formula - sum of even number / count of even number 


start = 1
end = 100 
sum_of_even_number = 0
count_of_even_number = 0


while start <= end:
    # How to check even number
    if start % 2 == 0:
        sum_of_even_number = sum_of_even_number + start
        count_of_even_number = count_of_even_number + 1
    
    start = start + 1


average = sum_of_even_number // count_of_even_number

print("Average :", average )


# Patterns 1 ----------------------

start = 1
end = 5 
bag = ""

while start <= end:
    bag = bag + "*"
    print(bag)
    start+=1



# Multiplication table ---------------------
# Input - 3
# Output :
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12

table_of = 12

start = 1
while start <= 10:
    print(table_of, "*" , start ,"=", start * 3)
    start = start + 1


# ---------------------------BREAK------------------------------

# Guest example 
total_guest = 7 
start_guest = 1


while start_guest <= total_guest:
    if start_guest == 4:
        break

    print("Guest :", start_guest)
    start_guest = start_guest + 1


# total_guest = 7
# start_guest = 1 2 3 4 

# cond - 1 <= 7 - True 
# cond - 2 <= 7 - True 
# cond - 3 <= 7 - True
# cond - 4 <= 7 - True

# Output : 
# Guest : 1
# Guest : 2
# Guest : 3



# First number which is divisible by 3 between 50 - 70 

start = 50
while start <= 70:
    if start % 3 == 0:
        print(start)
        break
    start = start + 1



# ----------------- CONTINUE -----------------

# Guest Example
total_guest = 7
start = 1
sick_guest = 3

while start <= total_guest:

    if start == 3:
        start = start + 1
        continue
    
    print("Guest :", start)
    start = start + 1
    
# Printing numbers either not divisble by 3 or 5
# Way 1
start = 1
end = 50 

while start <= end:
    if start % 5 == 0 or start % 3 == 0:
        start = start + 1
        continue
    print(start)
    start = start + 1

# Way 2
start = 0
end = 50 

while start < end:
    start += 1
    if start % 3 == 0 or start % 5 == 0:
        continue
    print(start)