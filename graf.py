import matplotlib.pyplot as plt
import matplotlib.animation as animation



fig = plt. figure(figsize=(8, 8)) # Создаем окно
vals = [] # Массив значений
labels = [] # Массив названий

# Читаем из файла все страны с инфо о них
with open('files/info.txt', 'r', encoding='utf-8') as file:
    all_country_info = file.readlines()

# Пробегаемся по странам из списка
for country in all_country_info:
    country = country.replace(' ', '') # Убераем лишние пробелы
    info = country[0:-8].split(',') # Создаем массив с инфо о стране вида [рейтинг, название, население]
    #Заполняем массивы
    labels.append(f"{info[0]}. {info[1]}")
    vals.append(float(info[2]))

#рисуем диаграмму
plt.pie(vals, labels=labels, radius=1)
# Показываем окно
plt.show()