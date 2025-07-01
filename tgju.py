import requests
from bs4 import BeautifulSoup
from math import floor

__author__ = "MrMM7"

all_currencies  = [
  "USD",
  "EUR",
  "AED",
  "GBP",
  "TRY",
  "CHF",
  "CNY",
  "JPY",
  "KRW",
  "CAD",
  "AUD",
  "NZD",
  "SGD",
  "INR",
  "PKR",
  "IQD",
  "SYP",
  "AFN",
  "DKK",
  "SEK",
  "NOK",
  "SAR",
  "QAR",
  "OMR",
  "KWD",
  "BHD",
  "MYR",
  "THB",
  "HKD",
  "RUB",
  "AZN",
  "AMD",
  "GEL",
  "KGS",
  "TJS",
  "TMT"
];

all_gold: list[int] = [
    18,
    24
]

def every_currencies():
    return all_currencies 

def every_mineral():
    return all_gold

class InvalidCurrency(Exception):
    def __init__(self, message: str):
        print(message)

class InvalidMineral(Exception):
    def __init__(self, message: str):
        print(message)

class Currency_Rates:
    def __init__(self, currency: str):
        if len(currency) > 3: # if its longer than 3 letters like Dollar or Pound it instantly returns
            raise InvalidCurrency("Please only enter the first 3 letters (e.g USD, GBP, etc)")
        
        currency_exists = False
        for list_currency in all_currencies :
            if list_currency.lower() == currency.lower():
                currency_exists = True

        if not currency_exists:
            raise InvalidCurrency(f'{currency} is not a valid currency') 

        site_url = ""
         # for some reason the USD url is different than every other url so it has its own if statement
        if currency == 'USD':
            currency = 'dollar_rl'
            site_url = f'https://www.tgju.org/profile/price_{currency.lower()}'
        else:
            site_url = f'https://www.tgju.org/profile/price_{currency.lower()}'
        
        try:
            response = requests.get(site_url)
            response.raise_for_status()

            html = response.text

            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'})
            self.currency = int(price.text.replace(',', '')) #type: ignore

        except requests.exceptions.HTTPError:
            print('we hit a network error try again')
    
    def toman(self):
        # Return rate in toman for the currency
        return floor(self.currency / 10)
    def rial(self):
        # returns the rate in rial
        return self.currency
    


class Gold_Rates:
    def __init__(self, gold: int):
        if gold != 18 and gold != 24: # if its not 18 or 24 it returns
            raise InvalidCurrency("Please only enter the karrot like 18 and 24")
        
        site_url = f'https://www.tgju.org/profile/geram{gold}'
        try:
            response = requests.get(site_url)
            response.raise_for_status()
            html = response.text

            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'})

            self.rate: int = int(price.text.replace(',', '')) #type: ignore
        except requests.exceptions.HTTPError:
            print('we hit a network error try again')
    
    def toman(self):
        # Return rate in toman for the currency
        return floor(self.rate / 10)
    
    def rial(self):
        # returns the rate in rial
        return self.rate    


def get_currency_rate(currency: str):
    """Gives the price of the selected currency see the rial price with .rial() and toman price with .toman()"""
    return Currency_Rates(currency)

def get_gold_rate(karrot: int):
    """Gives the of the selected gold price see the rial price with .rial() and toman price with .toman()"""
    """only type the karrot not the starting \'geram\' """

    return Gold_Rates(karrot)


def test():
    print(get_currency_rate('USD').rial())
    print(get_gold_rate(18).rial())

if __name__ == "__main__":
    test()