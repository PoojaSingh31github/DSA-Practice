def custom_find(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    # print(str1_len, str2_len)
    # print("sdfvgbhnjmk", str1_len - str2_len + 1)
    for i in range(str1_len - str2_len + 1):
        # print("zzzzz",str1[i:i+str2_len])
        if str1[i:i + str2_len] == str2:
            return i
    return -1


str1 = 'Look for the substring in this string.'
str2 = 'substring'


output = custom_find(str1, str2)
print(output)  
