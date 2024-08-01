n=9
arr=[1, 8, 6, 2, 5, 4, 8, 3, 7]

maximum=0
for i in range(n):
    for j in range(i+1,n):
        height = min(arr[i],arr[i])
        width= j-i
        area = height*width
        maximum=max(maximum,area)
print(maximum)        




