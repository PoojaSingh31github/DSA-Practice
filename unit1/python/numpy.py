import numpy as np
# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
sum_arr = arr1 + arr2
print(sum_arr)

# Element-wise multiplication
prod_arr = arr1 * arr2
print(prod_arr)
arr = np.array([1, 2, 3, 4, 5])

# Square root of each element
sqrt_arr = np.sqrt(arr)
print(sqrt_arr)

# Exponential (e^x) of each element
exp_arr = np.exp(arr)
print(exp_arr)

# Sum of all elements
sum_all = np.sum(arr)
print(sum_all)
arr = np.array([1, 2, 3, 4, 5])

# Accessing the first element
print(arr[0])

# Slicing from index 1 to 3
print(arr[1:4])
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshaping to a 2x3 array
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
# Array of zeros
zeros_arr = np.zeros((3, 3))
print(zeros_arr)

# Array of ones
ones_arr = np.ones((2, 4))
print(ones_arr)

# Array with a range of numbers
range_arr = np.arange(1, 10, 2)
print(range_arr)
# Array with random values between 0 and 1
random_arr = np.random.rand(3, 3)
print(random_arr)

# Array with random integers
random_int_arr = np.random.randint(1, 10, size=(2, 5))
print(random_int_arr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])

# Broadcasting the vector to each row of the array
broadcasted_sum = arr + vector
print(broadcasted_sum)
# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)
print(matrix_product)

# Transpose of a matrix
transpose_matrix = matrix1.T
print(transpose_matrix)
