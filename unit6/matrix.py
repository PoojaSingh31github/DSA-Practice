matrix = [
    [2, 7, 10],
    [3, 6, 11],
    [4, 5, 12]
]
target =6

n=len(matrix)
m=len(matrix[0])

for j in range(m):
    for i in range(n-1,-1,-1):
        print(matrix[i][j], end=" ")
print("asdfghjkl")    
    
for j in range(m-1,-1,-1):
    for i in range(n):
        print(matrix[i][j], end=" ")
print("asdfghjkl") 
 
       
for j in range(m-1,-1,-1):
    for i in range(n-1,-1,-1):
        print(matrix[i][j], end=" ")
print("asdfghjkl")

# =======================================================================================================
# ==========================================================================================================

print("Specic Diagonals")            

a,b=0,0
for i in range(n):
  for j in range(m):
    if matrix[i][j]==target:
      a , b = i , j 
      
bag1=""
bag2=""
for i in range(n):      
  for j in range(m):
    if a-b ==i-j:
      bag1+=str(matrix[i][j])+" "
    if a+b==i+j:
      bag2+=str(matrix[i][j])+" "
print(bag1)
print(bag2)    
  
# =======================================================================================================
# ==========================================================================================================          
        
print("Corner Column Sum")      
s=0      
for j in range(m):
  for i in range(n):
    if j==0 or j==m-1:
      s+=matrix[i][j]
print(s)  

# =======================================================================================================
# ==========================================================================================================

print("N traversal")
for i in range(n-1,-1,-1):
    print(matrix[i][0],end=" ")
    
for i in range(1,n):
    for j in range(1,m):
        if i==j:
            print(matrix[i][j],end=" ")

for i in range(n-2,-1,-1):
    print(matrix[i][n-1],end=" ")
print()  

# =======================================================================================================
# ==========================================================================================================
print("spiral traversal")
res=[]
left,right,top,bottom = 0,m-1,0,n-1

while left<=right and top<=bottom:
    for j in range(left, right+1):
        res.append(matrix[top][j])
    top+=1
            
    for i in range(top, bottom+1):
        res.append(matrix[i][right])
    right-=1

    if top <= bottom:
        for j in range(right, left-1,-1):
            res.append(matrix[bottom][j])
        bottom-=1
    if left <= right:
        for i in range(bottom, top-1,-1):
            res.append(matrix[i][left])
        left+=1
print(res)  

# =======================================================================================================
# ==========================================================================================================

print("digonal traversal") 
result = []
for d in range(2 * n - 1):
    r = 0 if d < n else d - n + 1
    c = d if d < n else n - 1

    while r < n and c >= 0:
        result.append(matrix[r][c])
        r += 1
        c -= 1

print(result)    
  
# second approch way of wrting 
res = []
for col in range(n):
    i,j =0,col
    while i<n and j>=0:
        res.append(matrix[i][j])
        i+=1
        j-=1

for row in range(1,n):
    i,j = row, n-1
    while i<n and j>=0:
        res.append(matrix[i][j])
        i+=1
        j-=1
    
print(" ".join(map(str,res)))      