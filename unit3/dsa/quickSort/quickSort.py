# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)

# # Example usage
# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = quick_sort(arr)
# print("Sorted array:", sorted_arr)
def Partition(arr,l,r):
    pivot= arr[r]
    i=l-1
    for j in range(l,r):
        if arr[j]<=pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def quick_sort(arr,l,r):
    if l<r:
        p=Partition(arr,l,r)
        quick_sort(arr,l,p-1)
        quick_sort(arr,p+1,r)

arr=[10, 7, 8, 9, 1, 5]
n=len(arr)
quick_sort(arr,0,n-1)
print(arr)