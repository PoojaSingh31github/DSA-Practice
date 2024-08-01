#here first i'm taking value from the user side and it must not be an negetive number second i'm appling an discount of 10% on it and then subtracting from the price here if value is less than 20 that time it will not show any discount but if it is 20 and more than 20 that time only discount can bee apply.


price = int(input("enter the price of the item: $"))
discount = 10/100*price
if price >=0:
    if price>20:
     print( price - discount)
    else:
     print(price) 
else:
  print("Invalid input, the price must be a non-negative number.")     

   