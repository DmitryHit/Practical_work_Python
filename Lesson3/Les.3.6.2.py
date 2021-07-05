import string


def int_func():
    s = input("Введите слово: ")
    s2 = string.capwords(s)
    return s2


s_inp = int_func()
print(s_inp)
