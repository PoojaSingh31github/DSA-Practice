# star pattern 
matrix = [
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [9, 10, 11, 12, 13],
    [13,12,13,14,15],
    [13,12,13,14,15],
    ]
count=0
for i in range(5):
    count+=matrix[i][i]
print(count)
count=0
for i in range(5):
    count+=matrix[i][i]
print(count)


count=0
for i in range(5):
    count+=matrix[i][0]
print(count) 

count=0       
for i in range(5):
    count+=matrix[0][i]
print(count)    