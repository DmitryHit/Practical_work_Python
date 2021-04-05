from itertools import count, cycle

for el in count(int(input('Введите число: '))):
    if el >= 10:
        break
    else:
        print(el)


my_list = [10, 20, 30]

start = 0
stop = 10
for el in cycle(my_list):
    if start >= stop:
        break
    else:
        print(el)
        start += 1
