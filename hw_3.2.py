'hw_3.2'

list1 = [12, 3, 4, 10, 5]
# list1 = [1]
# list1 = []

if len(list1) == 0:
    print('Empty list')
elif len(list1) == 1:
    print(list1)
else:
    temp = list1[-1]
    list1 = [temp] + list1[:-1]

print(list1)