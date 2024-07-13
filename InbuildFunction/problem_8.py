list= [1, 2, 3, 4, 5]
str= 'hello'

def reverseTheInput(input):
    rev=[]
    for i in range(len(input)-1, -1, -1):
        rev.append(input[i])
    return rev
output_list=reverseTheInput(list)
print(output_list)

def reverseForStr(string):
    rev=""
    for i in range(len(string)-1,-1,-1):
        rev=rev+string[i]
    return rev    

output_str=reverseForStr(str)
print(output_str)

    