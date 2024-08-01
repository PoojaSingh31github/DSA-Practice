l = [1, 2, 2, 3, 4, 2]
str= 'hello world'


def custom_count(list, ele):
    count = 0
    for i in list:
        if i == ele:
            count += 1
    return count

fun_call_list=custom_count(l,2)
fun_call_str=custom_count(str,"o")

print(fun_call_list)
print(fun_call_str)

