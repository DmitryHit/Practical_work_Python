num_list = [12, 4, 7, 58, 31, 2, 5, 40, 5, 30, 150, 11, 335]
final_list = [num_list[el] for el in range(1, len(num_list)) if num_list[el] > num_list[el-1]]

print(f"Итоговый список - {final_list}")
