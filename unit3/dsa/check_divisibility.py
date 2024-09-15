def check_divisibility(n, k, arr):
    def generate_sums(index, current_sum):
        if index == len(arr):
            if current_sum != 0 and current_sum % k == 0:
                return True
            return False
        if generate_sums(index + 1, current_sum + arr[index]):
            return True
        if generate_sums(index + 1, current_sum):
            return True
        return False
    if generate_sums(0, 0):
        return "YES"
    else:
        return "NO"
T = int(input())  
for _ in range(T):
    n, k = map(int, input().split())  
    arr = list(map(int, input().split()))  
    print(check_divisibility(n, k, arr))  
