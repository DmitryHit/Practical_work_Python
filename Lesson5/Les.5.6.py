lesson = {}
with open("text_5_6.txt", encoding="utf-8") as sum_less:
    lines = sum_less.readlines()
    for line in lines:
        data = line.replace("(", " ").split()

        lesson[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

print(lesson)
