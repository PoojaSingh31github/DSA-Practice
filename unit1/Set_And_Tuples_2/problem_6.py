Set1 = {10, 20, 30, 40, 50}
Set2 = {30, 40, 60, 70}
Set3 = {50, 60, 90}

list1 = list(Set1)
list2 = list(Set2)
list3 = list(Set3)
    
# Step 1: Compare list1 with list2
temp_list = []
# for elem in list1:
#     if elem not in list2:
#         temp_list.append(elem)

# # Step 2: Compare temp_list with list3
# final_list = []
# for elem in temp_list:
#     if elem not in list3:
#         final_list.append(elem)
# print(final_list) 
for el in list1:
    if el in list1 and el not in list2 and el not in list3:
        temp_list.append(el)

print(temp_list)  



res=()

