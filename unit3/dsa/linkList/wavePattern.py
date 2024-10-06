# def wave_sort(arr):
#     # Sort the array first
#     arr.sort()
    
#     # Swap adjacent elements
#     for i in range(1, len(arr), 2):
#         # Swap arr[i] with arr[i-1]
#         if i < len(arr):
#             arr[i], arr[i-1] = arr[i-1], arr[i]

#     return arr

# # Example usage:
# arr = [1, 3, 2, 4, 5, 6]
# print("Original array:", arr)
# wave_sorted_array = wave_sort(arr)
# print("Wave sorted array:", wave_sorted_array)
def wave_sort_without_sorting(arr):
    for i in range(0, len(arr) - 1, 2):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if i > 0 and arr[i - 1] < arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr

# Example usage:
arr = [1, 3, 2, 4, 5, 6]
print("Original array:", arr)
wave_sorted_array = wave_sort_without_sorting(arr)
print("Wave sorted array without sorting:", wave_sorted_array)

