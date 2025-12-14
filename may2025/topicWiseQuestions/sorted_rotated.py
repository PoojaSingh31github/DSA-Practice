def is_sorted_and_rotated(arr):
    def find_min_index(arr):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < arr[(mid - 1) % len(arr)] and arr[mid] < arr[(mid + 1) % len(arr)]:
                return mid
            elif arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        return 0
    
    min_index = find_min_index(arr)
    return arr[:min_index] == sorted(arr[:min_index]) and arr[min_index:] == sorted(arr[min_index:])

arr = [3, 4, 5, 1, 2]
print(is_sorted_and_rotated(arr))  # Output: True
