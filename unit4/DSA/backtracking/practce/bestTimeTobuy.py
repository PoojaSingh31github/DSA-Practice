# arr = [7,2,3,4,5,6,7]

# mini=arr[0]
# profit=0
# for i in range(1,len(arr)):
#     diff = arr[i] - mini
#     profit = max(profit, diff)
#     mini= min(mini, arr[i])
# print(profit)  

# jump
def cal(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            return True
    return False
arr  = [2,3,1,1,4]
print(cal(arr))
