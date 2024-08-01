import math

print("H   H EEEEE L     L      OOO       W   W  OOO  RRRR  L     DDDD  !!")
print("H   H E     L     L     O   O      W W W O   O R   R L     D   D !! ")
print("HHHHH EEEEE L     L     O   O      W W W O   O RRRR  L     D   D !! ")
print("H   H E     L     L     O   O  ,,   W W  O   O R   R L     D   D  ")  
print("H   H EEEEE LLLLL LLLLL  OOO  ,,    W W   OOO  R   R LLLLL DDDD  !!")

# Numeric Types
an_integer = 10
a_float = 20.5
a_complex = 1 + 2j

# Sequence Types
a_string = "Hello, World!"
a_list = [1, 2, 3, 4, 5]
a_tuple = (1, 2, 3, 4, 5)
a_range = range(5)

# Mapping Type
a_dict = {"name": "Alice", "age": 25}

# Set Types
a_set = {1, 2, 3, 4, 5}
a_frozenset = frozenset({1, 2, 3, 4, 5})


# Boolean Type
a_bool = True

# Binary Types
a_bytes = b"Hello"
a_bytearray = bytearray(b"Hello")
a_memoryview = memoryview(b"Hello")

# None Type
a_none = None

#condition oprator
a = 3
b = 5
c = 8
print(a == b)  # True
print(a != b)  # True
print(a > b)  # True
print(a < b)  # True
print(a >= b)  # True
print(a <= b)  # True
print(a > b and c > a)  # True
print(a > b or c < b)  # True
a = False
print(not a)  # True
a_list = [1, 2, 3, 4, 5]
a_string = "Hello"

print(3 in a_list)        # True
print(6 not in a_list)    # True
print('H' in a_string)    # True
print('X' not in a_string) # True
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)       # True
print(a is c)       # False
print(a is not c)   # True
d = [1, 2, 3]

if a == c and b < a:
    print("a is equal to c, and b is less than a.")  # This will be printed

if a != b or b == c:
    print("a is not equal to b, or b is equal to c.")  # This will be printed

if not (a < b):
    print("a is not less than b.")  # This will be printed

if 2 in d and 4 not in d:
    print("2 is in the list and 4 is not in the list.")  # This will be printed

if a is not d:
    print("a is not the same object as d.")  # This will be printed
a = 10
b = 5
c = 3

# Addition
result_add = a + b
print("Addition:", result_add)  # 15

# Subtraction
result_sub = a - b
print("Subtraction:", result_sub)  # 5

# Multiplication
result_mul = a * b
print("Multiplication:", result_mul)  # 50

# Division
result_div = a / b
print("Division:", result_div)  # 2.0

# Floor Division
result_floor_div = a // c
print("Floor Division:", result_floor_div)  # 3

# Modulus
result_mod = a % c
print("Modulus:", result_mod)  # 1

# Exponentiation
result_exp = a ** c
print("Exponentiation:", result_exp)  # 1000

# Unary Plus
print("Unary Plus:", +a)  # 10

# Unary Minus
print("Unary Minus:", -a)  # -10

a = 3.4
b = 5.9

ceil_a = math.ceil(a)
ceil_b = math.ceil(b)

print(f"Ceiling of {a} is {ceil_a}")  # Ceiling of 3.4 is 4
print(f"Ceiling of {b} is {ceil_b}")  # Ceiling of 5.9 is 6
floor_a = math.floor(a)
floor_b = math.floor(b)

print(f"Floor of {a} is {floor_a}")  # Floor of 3.4 is 3
print(f"Floor of {b} is {floor_b}")  # Floor of 5.9 is 5