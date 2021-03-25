add_num = int(input("Введите натуральное число: "))
num_list = [7, 4, 3, 2]
tag = num_list.count(add_num)
for el in num_list:
    if tag > 0:
        i = num_list.index(add_num)
        num_list.insert(i+tag, add_num)
        break
    else:
        if add_num > el:
            j = num_list.index(el)
            num_list.insert(j, add_num)
            break
        elif add_num < num_list[len(num_list) - 1]:
            num_list.append(add_num)
print(num_list)
