def mr_robot(string,l,r):
    if l>r:
        return ""
    
    else:
        mid=l+(r-l)//2
        return string[mid] + mr_robot(string,l,mid-1) + mr_robot(string,mid+1,r)
    
string="abcdefghijk"
n=len(string)
ans=mr_robot(string,0,n-1)
print(ans)