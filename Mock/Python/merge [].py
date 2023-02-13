number_list1 = list(eval(input('number_list1[]=')))

number_list2 = list(eval(input('number_list2[]=')))

res_list = []

for x in number_list1:
    if x % 2 != 0:
        res_list.append(x)

for x in number_list2:
    if x % 2 == 0:
        res_list.append(x)

print('merge List:', res_list)
