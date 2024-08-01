Input = [1, 2, 3, 4, 5]
# print(Input.index(3))

def custom_index(lst, search_value):
    for i, value in enumerate(lst):
        if value == search_value:
            return i
    raise ValueError(f"{search_value} is not in list")

Input = [1, 2, 3, 4, 5]
index_of = custom_index(Input, 3)
print(index_of)