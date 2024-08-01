# Problem1_AreaCalculator.py in this problem i need to find the area of triangle which is area = base X heigth / 2 here i first take value from user an which is in string form so that one i converted into the integer value and by using formula i got the area of triangle.
base= int(input("enter base of triangle: "))
height = int(input("enter heigth of trangle: "))
if base >=0 and height>=0:
    area = base*height/2
    print(area)
else:
    print("Invalid input, base and height must be positive numbers.")    




# aftre this i passed my all test case:-
# Test Case 1: base = 10, height = 5. Expected output: "The area of the triangle is: 25.0"
# Test Case 2: base = 0, height = 15. Expected output: "The area of the triangle is: 0.0"
# Test Case 3: base = 8, height = 0. Expected output: "The area of the triangle is: 0.0"

# and then for my these :- 
# Edge Case 1: What happens if one or both inputs are zero? The output should be 0.0, as this represents a triangle with no area.
# Edge Case 2: What if negative values are entered? The program should handle this by printing: "Invalid input, base and height must be positive numbers."