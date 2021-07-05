def my_func(x, y):

    if y == 0:
        return 1.0

    if y < 0:
        y *= -1

    return 1.0 / (x ** y)


print(my_func(x=int(input("Введите число:")),
              y=int(input("Введите степень:"))))
