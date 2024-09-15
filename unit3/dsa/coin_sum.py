def find_sums(arr):
    s = set()
    s.add(0)  
    for i in arr:
        current_sums = list(s)
        for s in current_sums:
            s.add(s + i) 
    s.discard(0)
    distinct_sums = sorted(s)
    print(len(distinct_sums))  
    print(*distinct_sums)  
n = 3  
arr = [3,5,2]
# 3 5 2   

find_sums(arr)
