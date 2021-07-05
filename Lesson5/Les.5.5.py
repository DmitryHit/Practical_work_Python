try:
    with open("text_5_5.txt", "w+") as num_sum:
        user_input = input("Введите набор чисел через пробел: ")
        num_sum.writelines(user_input)
        summary = user_input.split()

        print(sum(map(int, summary)))
except ValueError:
    print("Нужно вводить числа приятель...")



