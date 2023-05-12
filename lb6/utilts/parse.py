# Импорты библиотек необходимые для парсинга
import requests
from bs4 import BeautifulSoup as bs

# User-agent чтобы сайт принимал нас за пользователя а не за машину
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# Класс генерирующий все числа от 0 до 9
class All_Num:
    all_num = [str(i) for i in range(0, 10)]

# Функция очистки файла от предыдущих использований
def clear_file():
    with open('files/info.txt', 'w') as file:
        file.close()

# Функция парсер
def parse():
    responce = requests.get(url='https://worldgeo.ru/lists/?id=3&loc=europe', headers=headers)
    soup = bs(responce.text, 'lxml') # Из ответа сайта получаем результат и переводим в нужный формат
    table = soup.find('table', class_='tbl') # Находим таблицу с данными
    all_country = table.find('tbody').find_all('tr') # Собираем данные по всем странам
    for country in all_country: # Пробегаемся по странам
        country_all_info = country.find_all('td') # Вся необходимая информация по стране
        country_rate = country_all_info[0].text # Рейтинг страны
        country_name = country_all_info[1].text #  название страны
        country_people_err = country_all_info[2].text # Население страны в неудобном формате
        words = ''
        # Пробегаемся по всем символам и заменяем , на . и убераем кодек
        for b in country_people_err:
            if b in All_Num.all_num:
                words += b
            elif b ==',':
                words += '.'
        
        country_people = words # Население страны в удобном формате
        with open('files/info.txt', 'a', encoding='utf-8') as file:
            file.write(f"{country_rate}, {country_name}, {country_people} тыс.чел\n")
        
def main():
    clear_file() # Запускаем функцию отчистки файла
    parse() # Запускаем функция парсинга

if __name__ == "__main__":
    main()