from functools import reduce


my_list = [el for el in range(100, 1001) if el % 2 == 0]


print(f"Чётные числа - {my_list}")
print(f"Произведение всех чисел - {reduce(lambda a, b: a * b, my_list)}")

"""
Так как условие имеет конечный вид, и список чисел останется неизменным, 
можно так же найти все чётные числа используя шаг, не знаю насколько это правильно, но тем не менее.
"""
my_list = [el for el in range(100, 1001, 2)]
print(f"Чётные числа, шаг - {my_list}")
