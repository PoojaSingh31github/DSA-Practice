def subset(n,s,i,curr):  #0  1  
    if i==n:
        return
    curr.append(s[i])
    print(curr)
    subset(n,s,i+1,curr)
    curr.pop()
    subset(n,s,i+1,curr)

n=3
s="abc"
ans = subset(n,s,0,[])
print(ans)

