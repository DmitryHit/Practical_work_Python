income = float(input("Введите выручку: "))
cost = float(input("Введите расходы на содержание фирмы: "))
if income > cost:
    profit = income - cost
    profitability = profit / income
    print("Фирма работает с прибылью:", profit)
    print("Рентабельнотсь фирмы:", profitability)
    employees = int(input("Введите количество сотрудников фирмы: "))
    profit_employees = profit / employees
    print("Прибыль в расчете на одного сторудника сотавила:", profit_employees)
elif cost > income:
    lesion = cost - income
print("К сожалению Ваша фирма работает в убыток.")
