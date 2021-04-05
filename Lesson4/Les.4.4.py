num_list = [33, 5, 17, 17, 27, 36, 33, 5, 34, 12, 83, 3, 25, 94]
no_repeat = [num for num in num_list if num_list.count(num) == 1]
print(f"Элементы не имеющие повторений - {no_repeat}")
