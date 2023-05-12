import requests
from bs4 import BeautifulSoup as bs


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}


class All_Num:
    all_num = [str(i) for i in range(0, 10)]

def clear_file():
    with open('files/info.txt', 'w') as file:
        file.close()

def parse():
    responce = requests.get(url='https://worldgeo.ru/lists/?id=3&loc=europe', headers=headers)
    soup = bs(responce.text, 'lxml')
    table = soup.find('table', class_='tbl')
    all_country = table.find('tbody').find_all('tr')
    for country in all_country:
        country_all_info = country.find_all('td')
        country_rate = country_all_info[0].text
        country_name = country_all_info[1].text
        country_people_err = country_all_info[2].text
        words = ''
        for b in country_people_err:
            if b in All_Num.all_num:
                words += b
            elif b ==',':
                words += '.'
            
        country_people = words
        with open('files/info.txt', 'a', encoding='utf-8') as file:
            file.write(f"{country_rate}, {country_name}, {country_people} тыс.чел\n")
        

def main():
    clear_file()
    parse()

if __name__ == "__main__":
    main()