user_str = input("Введите текс: ")
a = user_str.split(' ')
for i, us_str in enumerate(a, 1):
    if len(us_str) > 10:
        us_str = us_str[0:10]
    print(f"{i}. - {us_str}")
