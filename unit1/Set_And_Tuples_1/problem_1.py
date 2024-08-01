l=[1, 2, 2, 3, 4, 5, 3, 6, 4]
set_arr=set()
copied=set()
for i in l:
    if i in set_arr:
        copied.add(i)
    else:
        set_arr.add(i)

unique=set_arr-copied
print(list(unique))            

