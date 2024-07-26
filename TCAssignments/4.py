# row=3
# col=3
# matrix=[]
# for i in range(row):
#     m=[]
#     for j in range(col):
#         m.append(int(input(f"Enter element at position ({i}, {j}): ")))
#     matrix.append(m)
# print(matrix)        



# 90 degree
# 7 4 1 
# 8 5 2
# 9 6 3


mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r=len(mat)
c=len(mat[0])

for j in range(c):
    for i in range(r-1,-1,-1):
        print(mat[i][j], end=" ")
    print()  
# [1, 2, 3],
# [4, 5, 6], 
# [7, 8, 9]

# 180 degree
# 9 8 7 
# 6 5 4
# 3 2 1
for i in range(r-1,-1,-1):
    for j in range(c-1,-1,-1):
        print(mat[i][j], end=" ")
    print()  

def luckyNumbers(matrix):
    if not matrix or not matrix[0]:
        return []

    m = len(matrix)
    n = len(matrix[0])
    
    lucky = []

    # Find the minimum values in each row
    for i in range(m):
        min_r = min(matrix[i])
        min_c_index = matrix[i].index(min_r)

        # Check if the min value in this row is the maximum in its column
        is_lucky = True
        for j in range(m):
            if matrix[j][min_c_index] > min_r:
                is_lucky = False
                break

        if is_lucky:
            lucky.append(min_r)

    return lucky

# Example usage
matrix1 = [[3,7,8],[9,11,13],[15,16,17]]
# matrix2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# matrix3 = [[7,8],[1,2]]

print(luckyNumbers(matrix1))  # Output: [15]    
    