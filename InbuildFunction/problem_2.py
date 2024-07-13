def custom_rindex(list, item):
    for i in range(len(list) - 1, -1, -1):
        if list[i] == item:
            return i
    return -1

list = [1, 2, 3, 2, 4]
item = 2

print(custom_rindex(list, item))

