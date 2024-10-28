def backtrack(nums, path, result):
    if len(path) == len(nums):  
        result.append(path[:])  #result = [[1,2,3]]
        return

    for i in range(len(nums)):
        if nums[i] in path:  
            continue
        path.append(nums[i])  # path=[1,2,3]
        backtrack(nums, path, result)  
        path.pop()

def generate_permutations(nums):
    result = []
    backtrack(nums, [], result)  
    return result


nums = [1, 2, 3] 
permutations = generate_permutations(nums)

for perm in permutations:
    print(perm)