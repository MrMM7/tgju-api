# TGJU API For Python

This Python package scrapes real-time currency exchange rates and gold prices from [tgju.org](https://www.tgju.org) for the Iranian market. It provides both Rial and Toman values for all supported currencies , gold types and Cryptocurrencies.

## Features

- Get current exchange rates for 36+ currencies
- Get current gold prices for 18k and 24k gold
- Get the current price of the latest crypto in USD
- Comprehensive error handling
- Simple and intuitive API

## Installation

1.  Clone the project:

    ```
    git clone https://github.com/MrMM7/tgju-api.git
    ```

2.  Install required packages:

    ```
    pip install requests beautifulsoup4
    ```

## Supported Currencies and Gold Types

### Currencies

```
USD, EUR, AED, GBP, TRY, CHF, CNY, JPY, KRW, CAD, AUD, NZD, SGD, INR,
PKR, IQD, SYP, AFN, DKK, SEK, NOK, SAR, QAR, OMR, KWD, BHD, MYR, THB,
HKD, RUB, AZN, AMD, GEL, KGS, TJS, TMT
```

### Gold Karats

- 18k
- 24k

### Crypto

- BTC
- ETH
- Every coin that is available on [tgju.org](https://tgju.org).
  
## Usage

### Importing the Module

```
from tgju import get_rate
```

### Getting Rates
```python
# simply put the URL suffix example: https://www.tgju.org/profile/ geram18 <--
gold = get_rate('geram18')
print(f"Gold rate in rial: {gold}")
```

## Returns
by default every number returned by the ```get_rate()``` function is in rial <em>however</em> for crypto 
it is in USD because that's the way they are represented on the site.

## Example Output

```
USD in Rials: 1,178,600.0
18k Gold per gram (Rials): 111,536,000.0
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on [GitHub](https://github.com/MrMM7/tgju-api).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This package scrapes data from [tgju.org](https://tgju.org). Use it at your own risk. I The developer am not responsible for any financial decisions made based on this data. Always verify rates with official sources before making any transactions.

Please use this tool responsibly. Excessive requests or abuse may result in tgju.org generously gifting you with an **IP ban**.

