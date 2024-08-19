s1={1,2,3,4,7,5}
s2={10,22,3,35,7,6,24,6,5}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

arr=[1 , 4 , 3, 2 , 5 , 7]
k=9
n=len(arr)

for i in range(n):
    for j in range(i+1,n):
        sub_arr=arr[i:j]
        sum_of_arr=sum(sub_arr)
        print(sum_of_arr)
        
    if sum_of_arr==k:
        print(True)
            
list=[1,2,3,4,5]
list.extend([1,2,3,4])
list.append(1)
list.insert(3,355)
print(list)
