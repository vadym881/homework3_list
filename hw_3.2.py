'hw_3.2'
# list1 = [12, 3, 4, 10, 5]
# list1 = [1]
list1 = []
if len(list1) == 0:
    print('Empty list')
else:
    temp = list1[-1]
    list_result = [temp]
    list1.remove(temp)
    list1.insert(0, temp)

print(list1)