s="{([]()(]))}"
st=[]
flag =True
if len(s) ==1: flag = False
for i in s:
    if i in "{[(":
        st.append(i)
    else:
        if st:
            ch=st.pop()
            if i=="}" and ch!="{":
                flag= False
            elif i=="]" and ch!="[":
                flag= False
            elif i==")" and ch!="(":
                flag= False
print(flag)            