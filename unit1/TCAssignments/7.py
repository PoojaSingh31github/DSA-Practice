# defination = key value pair , {}, 
# user case 
# methods 


dic={
    "1": 2,
    "2":4,
    "3":6,
    "4":1
}
print(dic.clear())
a=[1,2,3,4]
for i in range(len(a)-1,-1,-1):
    print(a[i])

arr=[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
r=3
c=4
top,bottom,left,right = 0,r-1,0,c-1
for i in range(bottom,top-1,-1):
    print(arr[left][i], end=" ")

