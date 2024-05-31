'hw_3.3'
# list_init = [1, 2, 3, 4, 5, 6]
list_init = [1, 2, 3, 4, 5, 6, 7]
# list_init = [1]
# list_init = []
len_list = len(list_init)
limit1 = 0
limit2 = 0
if len_list % 2 == 0:
    limit1 = limit2 = int(len_list/2)
else:
    limit1 = int(len_list/2) + 1
    limit2 = len_list - limit1 + 1

list1 = list_init[:limit1]
list2 = list_init[limit2:]
list_res = [list1, list2]
print(list_res)