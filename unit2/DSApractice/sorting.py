# bubble sort
array=[64, 34, 25, 12, 22, 11, 90]
n=len(array)
for i in range(n):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j], array[j+1]=array[j+1], array[j]
print(array)  
          
array=[64, 34, 25, 12, 22, 11, 90]

# selection sort
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if array[j]<array[min_index]:
            min_index=j
    array[i], array[min_index] = array[min_index],array[i]
print(array)            