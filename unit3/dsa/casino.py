def can_make_decks(T, n, m, k, max_time):
    count = 0 
    decks = 0 
    
    for i in range(n):
        if T[i] <= max_time: 
            count += 1
        else:
            count = 0  
        
        if count == k:
            decks += 1
            count = 0 
    
    return decks >= m  

def min_time_to_make_decks(T, n, m, k):
    low, high = 1, max(T)  
    
    if m * k > n:
        return -1  
    
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_make_decks(T, n, m, k, mid):
            result = mid
            high = mid - 1 
        else:
            low = mid + 1
    
    return result

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    T = list(map(int, input().split()))
    print(min_time_to_make_decks(T, n, m, k))
