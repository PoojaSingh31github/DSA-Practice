array=[1,2,3,4,5,6,7,8,9]

for i in range(len(array)):
    if array[i]%2==0:
        continue
    else:
        print(array[i])