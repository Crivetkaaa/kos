import requests
from bs4 import BeautifulSoup as bs


class Global:
    data = []
    headers  = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    all_info = {}
    kall_info = {}

def parse():
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = requests.get(url=url, headers=Global.headers)
    soup = bs(response.text, 'lxml')
    all_currencies_table = soup.find('table', class_="data")
    all_currencies_list = all_currencies_table.find_all('tr')
    for currencies in all_currencies_list:
        currencies_info = currencies.find_all('td')
        # аbbreviation = 
        if currencies_info != []:
            word = ''
            for b in currencies_info[4].text:
                if b != ',':
                    word += b
                else:
                    word += '.'
            kyrs = float(word) / int(currencies_info[2].text)
            Global.data.append(currencies_info[1].text)
            
            Global.all_info[currencies_info[1].text] = {
                'currencies': currencies_info[3].text,
                "exchange_rates": kyrs 
            }
            Global.kall_info[currencies_info[3].text] = {
                "exchange_rates": kyrs 
            }
        

def main():
    parse()


if __name__ == "__main__":
    main()