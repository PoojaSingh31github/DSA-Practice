dic ={
    '2':"abc",
    '3':"def",
    '4':"ghi",
    '5':"jkl",
    '6':"mno",
    '7':"pqrs",
    '8':"tuv",
    '9':"wxyz"
}

def genSeq(n,i,curr,res):
    if i==len(n):
        res.append(curr)
        return
    char = dic[n[i]]
    for c in char:
        genSeq(n,i+1,curr+c,res)


def comb(n):
    if len(n)==0:
        return []
    res=[]
    genSeq(n,0,"",res)
    return res

n="23"
ans=comb(n)
print(ans)
