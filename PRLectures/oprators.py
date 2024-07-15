
# If if is raining we will watch movie
# Create a variable to store raing status 
is_raining = False 
if is_raining :
    print("Lets watch a movie")


# If block only runs if the condition is true 
# print("Code Start")

# if True:
# 	print("Condition is true")

# print("Code End")



# How to check if a number is greater or not 
a = 5 
b = 3
if a > b:
  print("A is greater than B")


# How to check if two numbers are equal or not 
a = 10 
b = 10
if a == b:
    print("Both a and b are equal number")

# How to check two names are equal or not 
name1 = "Rahul"
name2 = "Rahul"

if name1 == name2:
  print("Both Names are same")



# ------------------------------------------if else---------------------------------------


# Amazon shopping shipping charge on total price 
total_price = 300

if total_price > 500:
    print("Free shipping")
else:
    print("Rs:50 applicable for shipping charge")


# User login in your application
is_login = False
if is_login:
    print("You can buy products now..")
else:
    print("Please login for shopping")


# Payment from Paytm wallet 
wallet_balance = 1000
payment_request = 1500

if payment_request <= wallet_balance:
    print("Payment Success") 
else:
    print("Insufficient Balance")




# -------------------if , elif , else --------------

# Signal in Street 
signal_color = "Red"

if signal_color == "Red":
    print("Stop the car")
elif signal_color == "Green":
    print("Go on....")
elif signal_color == "Yellow":
    print("Red signal will appear soon")
else :
    print("Other color")



# Score report 
score = 80

if score >= 90:
    print("AA")
elif score >= 80:
    print("A+")
elif score >= 70:
    print("A")
elif score >= 60:
    print("B+")
elif score >= 50:
    print("B")
elif score >= 40:
    print("C+")
elif score >= 30:
    print("C")
else:
    print("Fail")


# Discount problem 

shopping_bill = 55000

if shopping_bill >5000:
    print("You will get 10% discount")
elif shopping_bill >15000:
    print("You will get 20% discount")
elif shopping_bill >30000:
    print("You will get 30% discount")
elif shopping_bill > 50000:
    print("You will get 35% discount with Surprise Gifts")


shopping_bill = 55000

if shopping_bill > 50000:
    print("You will get 35% discount with Surprise Gifts")
elif shopping_bill > 30000:
    print("You will get 30% discount")
elif shopping_bill > 15000:
    print("You will get 20% discount")
elif shopping_bill >5000:
    print("You will get 10% discount")




# --------- if if vs if elif ------------------

# if elif 

rice_availaible = False
wheat_availaible = True
apple_availaible = True


if rice_availaible:
  print("Buy rice")
elif wheat_availaible:
  print("Buy Wheat")
elif apple_availaible:
  print("Buy apple")
else:
  print("Nothing is available")



# if if 

rice_available = True 
wheat_available = True
apple_available = False

if rice_available:
  print("Buy rice")
if wheat_available:
  print("Buy Wheat")
if apple_available:
  print("Buy apple")


# ----------------- Nested if -------------------
# Marriage problem 
age = 17
gender = "female"


if gender == "male":
    if age >= 21:
        print("You can marry")
    else:
        print("You can not marry")
elif gender == "female":
    if age >=18:
        print("You can marry")
    else:
        print("You can not marry")



# Database
stored_username = "pablo"
stored_password = "pablo@123"


input_username = "pablo"
input_password = "Pablo@123"


if stored_username == input_username:
    if stored_password == input_password:
        print("Login....")
    else:
        print("Incorrect password")
else:
    print("User not exist")


# ---------- Logical operators : and ------------------- 

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False


# Palak paneer 
palak_availaible = True 
paneer_available = True

if palak_availaible and paneer_available:
    print("We will have palak paneer today")
else:
    print("Something else other than palak paneer")



# Marriage Problem 
gender = "male"
age = 18

if gender == "male" and age >= 21 :
    print("Can marry")
elif gender == "female" and age >= 18:
    print("Can marry")
else:
    print("Can't marry")


# Which number is greater 
num1 = 10 
num2 = 20
num3 = 30

if num1 > num2 and num1 > num3:
    print("Num1 is greater")
elif num2 > num1 and num2 > num3:
    print("Num2 is greater")
else:
    print("Num3 is greater")


# Teenage or Twenties
year_of_birth = 1999
age = 2024 - year_of_birth

if age >= 13 and age <= 19:
    print("Teenage")
else:
    print("Twenties")




# Check if two number is even or not 
num1 = 7
num2 = 11 

if num1 % 2 == 0 and num2 % 2 == 0 :
    print("Both are even number")
elif num1 % 2 == 0 :
    print("Only num1 is even")
elif num2 % 2 == 0 :
    print("Only num2 is even")
else:
    print("Both are odd")


# ---------- Logical operators : or ------------------- 

# Dinner possibility
potato_available = True 
paneer_available = False

if potato_available or paneer_available:
    print("Dinner is possible today")
else:
    print("Today dinner is not possible")


# choosing a Snack 
snack = "samosa"
if snack =="samosa" or snack == "pakora":
    print("Perfect snack time!")
else:
    print("Mood off")


# Marriage problem 
gender = "Female"
age = 18 

if (gender == "Female" and age >= 18) or (gender == "male" and age >= 21) :
    print("You can marry")
else:
    print("You can not marry")



char = "a"

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("Char is a vowel")
else:
    print("Not a vowel")


# ---------- not ---------------

admin_access = True
if not admin_access:
    print("Access denined")
else:
    print("Welcome")


