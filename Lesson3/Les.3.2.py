def user_data(**kwargs):
    return kwargs


print(user_data(name=input("Введите своё имя: "), surname=input("Введите свою фамилию: "),
                birth=input("Введите год своего рождения: "), city=input("Введите город в котором Вы проживаете: "),
                email=input("Введите свой email: "), phone=input("Введите номер своего телефона: ")))
