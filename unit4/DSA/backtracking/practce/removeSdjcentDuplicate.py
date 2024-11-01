def rremove(s):
    sb=""
    n=len(s)
    i=0
    while i<n:
        repeat = False
        while i+1<n and s[i]==s[i+1]:
            repeat = True
            i+=1
        if not repeat:
            sb+=s[i]
        i+=1
    return sb    
    
    
    
s = "geeksforgeek"
ans = rremove(s)
print(ans)
    
