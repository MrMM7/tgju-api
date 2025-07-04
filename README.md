# TGJU API For Python

This Python package scrapes real-time currency exchange rates and gold prices from [tgju.org](https://www.tgju.org) for the Iranian market. It provides both Rial and Toman values for all supported currencies , gold types and Cryptocurrencies.

## Features

- Get current exchange rates for 36+ currencies
- Get current gold prices for 18k and 24k gold
- Get the current price of the latest crypto in both USD and IRR
- Automatic value conversion between Rial and Toman
- Comprehensive error handling
- Simple and intuitive API

## Installation

1.  Clone the project:

    ```
    git clone https://github.com/MrMM7/tgju-api.git
    ```

2.  Install required packages:

    ```
    pip install requests beautifulsoup4 pycoingecko
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

because of the weird naming standards tgju uses you can't just write $BTC it has to be the full name WITH a $ sign behind it

- $bitcoin
- $ethereum
- ... etc
  
## Usage

### Importing the Module

```
from tgju import get_rate
```

### Getting Currency Rates

```
# Get USD rate
usd_rate = get_rate('USD')
# MUST choose either .rial() or .toman()
print(f"USD in Rials: {usd_rate.rial():,}")
print(f"USD in Tomans: {usd_rate.toman():,}")
```

### Getting Gold Rates

```
# Get 18k gold rate
gold_18k = get_rate(18)
# MUST choose either .rial() or .toman()
print(f"18k Gold per gram (Rials): {gold_18k.rial():,}")
print(f"18k Gold per gram (Tomans): {gold_18k.toman():,}")
```

### Getting Crypto Rates

```
# Get BTC rate
btc_rate = get_rate('$bitcoin')
# MUST write .dollar() or alternatively use the automatic conversion to IRR using .rial() or .toman()
print(f"BTC in Dollars: {btc_rate.dollar():,}")
print(f"BTC in Rials: {btc_rate.rial():,}")
print(f"BTC in Tomans: {btc_rate.toman():,}")
```

Note: crypto names that are longer than one word like "baby doge coin" don't work please only use single word ones like bitcoin, ethereum, ... etc

## Why You MUST Choose `.rial()` or `.toman()`

In the Iranian currency system:

- **Rial (﷼)** is the official currency
- **Toman (تومان)** is an unofficial but widely used unit where:

  1 Toman = 10 Rials
  The conversion methods:

- `.rial()` returns the raw value in Iranian Rials
- `.toman()` converts the value to Tomans (dividing Rials by 10)
- `.dollar()` only works on Crypto but returns the current live USD price of it

You **must explicitly choose** between these methods because:

1.  Financial calculations require clear unit specification
2.  Automatic conversion could lead to dangerous financial errors
3.  Different use cases require different units (official vs common usage)
4.  Prevents ambiguity in financial reporting

## Error Handling

The package raises custom exceptions for invalid inputs:

```
try:
    # Attempt to get invalid currency
    get_rate('XYZ')
except InvalidCurrency as e:
    print(e)
try:
    # Attempt to get invalid gold karat
    get_rate(22)
except InvalidMineral as e:
    print(e)
try:
    # Attempt to get invalid crypto
    get_rate('$gooncoin')
except InvalidCrypto as e:
    print(e)
```

## Example Output

```
USD in Rials: 900,000
USD in Tomans: 90,000
18k Gold per gram (Rials): 70,000,000
18k Gold per gram (Tomans): 7,000,000
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on [GitHub](https://github.com/MrMM7/tgju-api).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This package scrapes data from [tgju.org](https://tgju.org). Use it at your own risk. I The developer am not responsible for any financial decisions made based on this data. Always verify rates with official sources before making any transactions.

Please use this tool responsibly. Excessive requests or abuse may result in tgju.org generously gifting you with an **IP ban**.

