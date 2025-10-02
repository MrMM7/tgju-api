# 2025 MrMM7 - See LICENSE to Learn more

import requests
from bs4 import BeautifulSoup
from typing import Union

# returns the live price of Gold in both 18k or 24k its up to the users choice
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

        def current_rate(self) -> float:
            return self.rate

    return Rates(link_suffix).current_rate()


# if it's an int it assumes that it's gold carrots if letter than currency
def get_rate(arg: Union[int, str]):
    try:
        if isinstance(arg, (int, str)):
            return rates(arg)
        else:
            raise ValueError('get_rate only accepts ints and strings')

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