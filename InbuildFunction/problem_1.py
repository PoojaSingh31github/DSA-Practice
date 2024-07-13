Input = ['Hello', 'World']

def joinfunc(Input):
    res=""
    for i,j in enumerate(Input):
        res+=j
        if i<len(Input)-1:
            res+=" "
    return res

func_call=joinfunc(Input)    
print(func_call)    
my_dict = {'apple': 2, 'banana': 3, 'orange': 1}
my_dict['apple'] = 5
print(my_dict['apple'])


def find_common_element(arr1, arr2):
    set_arr2 = set(arr2)
    for element in arr1:
        if element in set_arr2:
            return element

arr1 = [4, 5, 7]
arr2 = [9, 2, 5]
print(find_common_element(arr1, arr2))

def find_element_to_remove(arr):
    total_sum = sum(arr)
    for num in arr:
        if (total_sum - num) % 7 == 0:
            return num

A = [14, 21, 35]
print(find_element_to_remove(A))

def find_element_to_remove(arr):
    total_sum = sum(arr)
    for i, num in enumerate(arr):
        if (total_sum - num) % 7 == 0:
            return i

A = [2, 4, 5, 7]
print(find_element_to_remove(A))
def find_common_element(arr1, arr2):
    set_arr2 = set(arr2)
    for element in arr1:
        if element in set_arr2:
            return element

arr1 = [1, 2, 3]
arr2 = [4, 5, 3]
print(find_common_element(arr1, arr2))
def find_element_to_remove(arr):
    total_sum = sum(arr)
    smallest = float('inf')
    index_to_remove = -1

    for i, num in enumerate(arr):
        if (total_sum - num) % 7 == 0:
            if num < smallest:
                smallest = num
                index_to_remove = i

    return index_to_remove

A = [5, 10, 14]
print(find_element_to_remove(A))