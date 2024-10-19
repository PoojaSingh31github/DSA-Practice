# dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

# def gen_seq(N,index,current,result):
#   if index == len(N):
#     result.append(current)
#     return
  
#   char=dic[N[index]]
  
#   for i in char:
#     gen_seq(N,index+1,current+i,result)
  
# def comb(N):
#   if len(N)==0:
#     return []
  
#   result = []
#   gen_seq(N,0,'',result)
#   return result

# N=input()
# # print(type(N),N)
# ans=comb(N)
# ans.sort()
# print(*ans)


dic={
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
  }
def diff_com(n,i,curr,result):
  if i==len(n):
    result.append(curr)
    return
    
  char = dic[n[i]]
  
  for c in char:
    diff_com(n,i+1,curr+c,result) 
    
def combination(n):
  if len(n)==0:
    return []

  result =[]
  
  diff_com(n,0,"",result)
  return result
  
n=input()
ans=combination(n)
ans.sort()
print(*ans)