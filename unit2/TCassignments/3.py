mat = [
    [10, 19, 21, 32, 15, 5, 12],
    [10, 19, 21, 32, 15, 5, 12],
    [10, 19, 21, 32, 15, 5, 12],
    [10, 19, 21, 32, 15, 5, 12],
    [10, 19, 21, 32, 15, 5, 12],
    [10, 19, 21, 32, 15, 5, 12],
    [10, 19, 21, 32, 15, 5, 12],
    [10, 19, 21, 32, 15, 5, 12]
]

n=len(mat)
m=len(mat[0])
print(n,m)
for i in range(n-2):
    for j in range(2):
        # if mat[i][j]:
        print(mat[j][i],end=" ")

a,b=0,m-1
while a<n and b>=0:
    print(mat[a][b],end=" ")
    a+=1
    b-=1

for i in range(n-1,2,-1):
    for j in range(m-1,m-3,-1):
        print(mat[i][j],end=" ")

