time = int(input("Введите время в секундах: "))
sec = time
minutes = sec // 60
hours = minutes // 60
print(f"Столько секунд равно: {hours:02}:{minutes % 60:02}:{sec % 60:02}")
