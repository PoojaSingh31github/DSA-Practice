n=6
s="))(())"
st=[]
for i in range(n):
    if st and s[st[-1]-1]=="("and s[i]==")":
        st.append(st[-1])
    else:
        
        st.append(i+1)  
print(st)    


st="1 0 0 0 1"
for i in range(len(st)):
    if i=0 and st[i]==0 and st[len(st)-1]==