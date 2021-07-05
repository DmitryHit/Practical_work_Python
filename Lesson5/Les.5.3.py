with open("text_5_3.txt", "r", encoding="utf-8") as report:
    salary = []
    low_salary = []
    my_list = report.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < int(20000):
            low_salary.append(i[0])
        salary.append(i[1])
print(f"Оклад меньше 20000 - {low_salary}")
print(f"Cредний оклад - {int(sum(map(int, salary)) / len(salary))}")
