import matplotlib.pyplot as plt
import matplotlib.animation as animation



fig = plt. figure(figsize=(8, 8))
vals = []
labels = []

with open('files/info.txt', 'r', encoding='utf-8') as file:
    all_country_info = file.readlines()

for country in all_country_info:
    country = country.replace(' ', '')
    print(country)
    info = country[0:-8].split(',')
    print(info)

    labels.append(f"{info[0]}. {info[1]}")
    vals.append(float(info[2]))

plt.pie(vals, labels=labels, radius=1)
plt.show()