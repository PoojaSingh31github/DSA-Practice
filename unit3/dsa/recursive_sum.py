def sums(s):
    if s=="":
        return 1
    else:
        # print(arr,n-1)
        print(s)
        return 1+ sums(s.replace(s[0],""))



arr="pooja_singh"
ans=sums(arr)  
print(ans)  