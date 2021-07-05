def my_sum():
    sum_now = 0
    ex = False
    while not ex:
        num = input('Введите число или Q для выхода: - ').split()
        result = 0
        for el in range(len(num)):
            if num[el] in ['q', 'Q', 'й', 'Й']:
                ex = True
                break
            else:
                result = sum_now + int(num[el])
        sum_now = sum_now + result
        print(f'Сумма в настоящее время равна: {sum_now}')
    print(f'Итоговая сумма: {sum_now}')


my_sum()
