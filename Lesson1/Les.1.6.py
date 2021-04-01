a = float(input("Введите результаты пробежки первого дня в км: "))
b = float(input("Введите общий желаемый результат в км: "))
result_days = 1
result_km = a
print(f"{result_days}-й день: {a} км")
while result_km <= b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
    print(f"{result_days}-й день: {round(a, 2)} км")
print(f"Вы достигнете желаемого результата на %.d день." % result_days)
