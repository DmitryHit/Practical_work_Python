input_list = []
while True:
    user_input = input("Введите какой то текст: ")
    if user_input == "":
        print(input_list)
        exit()
    else:
        new_input = user_input + "\n"
        input_list.append(new_input)

    with open("text_5_1.txt", "w") as f:
        f.writelines(input_list)
