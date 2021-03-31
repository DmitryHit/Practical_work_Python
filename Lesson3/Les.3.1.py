def func_div():
    try:
        num_a = float(input("Введите первое число: "))
        num_b = float(input("Введите второе число: "))
        num_sum = num_a / num_b
    except ZeroDivisionError:
        return "На нуль не буду...И Вам не советую!"
    except ValueError:
        return "Необходимо ввести число!"
    return num_sum


ab_sum = func_div()
print(ab_sum)
