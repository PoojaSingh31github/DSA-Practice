
array=[64, 34, 25, 12, 22, 11, 90]
n=len(array)


# bubble sort
for i in range(n):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j], array[j+1]=array[j+1], array[j]
print(array)  


# selection sort
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if array[j]<array[min_index]:
            min_index=j
    array[i], array[min_index] = array[min_index],array[i]
print(array)   

# merge sort 
def divide(array):
    if len(array) <= 1:  # Base case
        return array
    mid = len(array)//2
    left =  divide(array[:mid]) 
    right =  divide(array[mid:]) 
    return merge(left,right)
    
    
def merge(left,right):
    
    sorted_arr =[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i+=1
            
        else:
            sorted_arr.append(right[j])
            j+=1
    
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr  

ans = divide(array)
print(ans)  

# quick sort

# insertion sort
for i in range(n):
    key = array[i]
    j=i-1
    while j>=0 and array[j] > key:
        array[j+1] = array[j]
        j-=1
    array[j+1] = key
print(array)
        
    


