def my_func(x, y):
    if y == 0:
        return 1.0
    if y < 0:
        y *= -1

    power = x
    for i in range(1, y):
        x *= power

    return 1.0 / x


print(my_func(x=int(input("Введите число:")),
              y=int(input("Введите степень:"))))
