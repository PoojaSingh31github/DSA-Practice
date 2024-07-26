l=[1,2,3,4,5,6,7,8,9]

# product=1*2*3*4*5*6*7*8*9
# print(product)
product=1
for i in l:
    # product=product*i
    product*=i

print(product)    
string = "hello"
result = string.upper()
print(result)


# 17
print(int(17**.5))

arr = [0,3,1,2,]
n = 4
dic={}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1       
print(dic)        
string=""
for i,j in dic.items():
    if j>1:
        string+=str(i)+" "
    else:
        string=str(-1)    

print(string)


# mat=[[1 2 3],[1 2 3],[1 2 3]]

def N_traversal(N,matrix):
    bag=""
    for i in range(N-1,-1,-1):
        bag=bag+str(matrix[i][0])+" "
    for i in range(1,N-1):
        for j in range(1,N-1):
            if i==j:
                bag=bag+str(matrix[i][j])+" "
    for i in range(N-1,-1,-1):
        bag=bag+str(matrix[i][N-1])+" "            
        
    print(bag) 
N_traversal(1,[1])
