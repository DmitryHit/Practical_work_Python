from itertools import count
from math import factorial


def fact_num():
    for el in count(1):
        yield factorial(el)


num_inp = fact_num()
a = 0
b = int(input("Введите число факториал которого Вы хотите получить: "))
for i in num_inp:
    if a < b:
        print(i)
        a += 1
    else:
        break
