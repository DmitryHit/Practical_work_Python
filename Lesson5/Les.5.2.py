with open("text_5_2.txt", encoding="utf-8") as f:
    line = 0
    for i in f:
        line += 1
        flag = 0
        word = 0
        for j in i:
            if j != " " and flag == 0:
                word += 1
                flag = 1
            elif j == " ":
                flag = 0
        print(f"Количество слов в строке: ", word)
print(f"Кол-во строк в файле: ", line)
