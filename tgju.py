import requests
from bs4 import BeautifulSoup
from math import floor
from typing import Union
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def crypto_exists(full_name: str) -> bool:
    full_name = full_name.lower()
    for coin in cg.get_coins_list():
        if coin['name'].lower() == full_name:
            return True
    return False

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
]

all_gold: list[int] = [
    18,
    24
]


def every_currencies():
    return all_currencies 


def every_mineral():
    return all_gold

# I couldn't figure out how to get every crypto so there is no every_crypto function

class InvalidCurrency(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidMineral(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidCrypto(Exception):
    def __init__(self, message: str):
        super().__init__(message)


# returns the currency rate of the requested currency by the user
def gold_rates(gold_type: int):

    class GoldRates:

        def __init__(self, gold: int):
            if gold != 18 and gold != 24: # if its not 18 or 24 it returns
                raise InvalidCurrency('Please only enter the karrot like 18 and 24')

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

        def rial(self):
            # returns the rate in rial
            return self.rate


    return GoldRates(gold_type).rial()
# returns the live price of Gold in both 18k or 24k its up to the users choice


# returns the live price of Gold in both 18k or 24k its up to the users choice
def currency_rates(currency_name: str):

    class CurrencyRates:

        def __init__(self, currency: str):
            if len(currency) > 3: # if its longer than 3 letters like Dollar or Pound it instantly returns
                raise InvalidCurrency('Please only enter the first 3 letters (e.g USD, GBP, etc)')

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


        def rial(self):
            # returns the rate in rial
            return self.currency

    return CurrencyRates(currency_name).rial()


def crypto_rates(crypto_name: str):

    class CryptoRates:

        def __init__(self, crypto: str):
            # the crypto is originally $bitcoin this removes the $ sign
            self.crypto = crypto[1:].lower().strip()
            if not crypto_exists(self.crypto):
                raise InvalidCrypto(f'{self.crypto} is not a valid crypto')

            site_url = f'https://www.tgju.org/profile/crypto-{self.crypto}'


            try:
                response = requests.get(site_url)
                response.raise_for_status()

                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

                current_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'})
                rate = current_price.text.replace(',','')
                self.rate = float(rate)


            except requests.exceptions.HTTPError:
                print('network error try again')


        def dollar(self):
            # returns the current price in USD
            return self.rate

    return CryptoRates(crypto_name).dollar()


# if it's an int it assumes that it's gold carrots if letter than currency
def get_rate(arg: Union[int, str]):
    """
    if the parameter is a int you'll get gold prices if letters than currency

    Parameter:
        arg: int or str
        Currency: str
        Crypto: "$" + str
        Gold: int

    Returns:
        Gold: (int) Rial: int,
        Currency: (str) Rial: int,
        Crypto: (str) Dollar: int

    """

    try:
        if isinstance(arg, int): 
            return gold_rates(arg)
        elif isinstance(arg, str):
            
            # if the string starts with '$' than it means that its crypto
            if arg[0] == '$':
                return crypto_rates(arg)

            # if it doesn't have '$' than its currency's
            else:
                return currency_rates(arg)

        else:
            raise ValueError('get_rate only accepts ints and strings')
    except ValueError as e:
        print(e)


# just testing the functionality of the code
def test():
    usd_rate = get_rate('USD')
    gold_rate = get_rate(18)
    bitcoin_rate = get_rate('$bitcoin')

    print(f'USD: {usd_rate:,}')
    print(f'Gold: {gold_rate:,}')
    print(f'BTC: {bitcoin_rate:,}')


if __name__ == "__main__":
    test()