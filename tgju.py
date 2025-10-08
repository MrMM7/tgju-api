# 2025 MrMM7 - See LICENSE to Learn more

import requests
from bs4 import BeautifulSoup
from typing import Union

# returns the live rate of whatever currency requested
def rates(link_suffix: str):

    class Rates:

        def __init__(self, suffix: str):
            site: str = f'https://www.tgju.org/profile/{suffix}'

            try:
                response = requests.get(site)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')
                self.rate = float(soup.find('span', {'data-col': "info.last_trade.PDrCotVal"}).string.strip().replace(',', ''))

            except requests.exceptions.RequestException as e:
                print(e)

        def get_current_rate(self) -> float:
            return self.rate

    return Rates(link_suffix).get_current_rate()


# the main function used to get rates
def get_rate(arg: str):
    """Returns the current available rate of the currency requested on the tgju.org website"""
  
    try:
        if isinstance(arg, str):
            return rates(arg)
        else:
            raise ValueError('get_rate only accepts strings')

    except ValueError as e:
        print(e)


# just testing the functionality of the code
def test():
    gold_rate = get_rate("geram18")
    usd_rate = get_rate("price_dollar_rl")
    bitcoin_rate = get_rate("crypto-bitcoin")
    oil_rate = get_rate("energy-brent-oil")

    print(f"Gold rate in rial: {gold_rate}")
    print(f"USD rate in rial: {usd_rate}")
    print(f"Bitcoin rate in rial: {bitcoin_rate}")
    print(f"Brent Oil rate in rial: {oil_rate}")


if __name__ == "__main__":
    test()
