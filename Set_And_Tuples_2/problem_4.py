set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}

def is_subset(subset, main_set):
    for element in subset:
        if element not in main_set:
            return False
    return True

print(is_subset(set1, set2)) 
