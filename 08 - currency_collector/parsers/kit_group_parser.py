from typing import List

from bs4 import BeautifulSoup
import requests

from parsers.bank import Bank


class KiGroupParser(Bank):
    def __init__(self, currencies: List, bank_url: str, bank_id: int):
        self.__currencies = {
            element[2]: (element[0], element[1]) for element in currencies
        }
        self.__bank_url = bank_url
        self.__bank_id = bank_id

    def __get_html(self):
        resp = requests.get(self.__bank_url)
        return resp.text

    def get_currency_rate(self):
        currency_rate = {
            'bank_id': self.__bank_id,
            'rate': []
        }

        html = self.__get_html()
        soup = BeautifulSoup(html, 'lxml')

        # contents = soup.find_all('li', {'class': 'currencies__block'})
        contents = soup.find_all('li', class_='currencies__block')
        for line in contents:
            name = line.find('div', {'class': 'currencies__block-name'}).find('a').text.split()[1]
            if not name.upper().endswith('/UAH') or name[:3].lower() not in self.__currencies:
                continue

            currency_id = self.__currencies[name[:3].lower()][0]
            purchase = (
                line.
                find('div', {'class': 'currencies__block-buy'}).
                find('div', {'class': 'currencies__block-num'}).
                text.strip())
            sale = (
                line.
                find('div', {'class': 'currencies__block-sale'}).
                find('div', {'class': 'currencies__block-num'}).
                text.strip()
            )

            currency_rate['rate'].append(
                {
                    'currency_id': currency_id,
                    'purchase': round(float(purchase), 2),
                    'sale': round(float(sale), 2)
                }
            )

        return currency_rate


if __name__ == '__main__':
    from connector import DbUtils
    from pprint import pprint

    db = DbUtils()
    db.connect()
    currency_list = db.get_currencies()
    id_bank, name_bank, url_bank = db.get_bank_by_id(4)
    db.close()
    parser = KiGroupParser(currency_list, url_bank, id_bank)
    pprint(parser.get_currency_rate())
