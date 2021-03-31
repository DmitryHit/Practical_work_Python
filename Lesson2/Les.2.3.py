season_list = ["Winter", "Spring", "Summer", "Autumn"]
my_dict = dict.fromkeys(season_list)
my_dict["Winter"] = [12, 1, 2]
my_dict["Spring"] = [3, 4, 5]
my_dict["Summer"] = [6, 7, 8]
my_dict["Autumn"] = [9, 10, 11]
season = int(input("Введите порядковый номер месяца по календарю: "))
if season == 1 or season == 2 or season == 12:
    print("Winter - Зима")
elif season == 3 or season == 4 or season == 5:
    print("Spring - Весна")
elif season == 6 or season == 7 or season == 8:
    print("Summer - Лето")
elif season == 9 or season == 10 or season == 11:
    print("Autumn - Осень")
else:
    print("Такого месяца к сожалению нет, приятель...")
