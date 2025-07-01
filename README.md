 # TGJU API For Python
 This Python package scrapes real-time currency exchange rates and gold prices from [tgju.org](https://www.tgju.org) for the Iranian market. It provides both Rial and Toman values for all supported currencies and gold types.
 ## Features
 
 - Get current exchange rates for 36+ currencies
 - Get current gold prices for 18k and 24k gold
 - Automatic value conversion between Rial and Toman
 - Comprehensive error handling
 - Simple and intuitive API
   
 ## Installation
 1. Clone the project:
    
    ```
    git clone https://github.com/MrMM7/tgju-api.git
    ```
 2. Install required packages:
    
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
 ## Usage
 ### Importing the Module
 ```
 from tgju import get_currency_rate, get_gold_rate
 ```
 ### Getting Currency Rates
 ```
 # Get USD rate
 usd_rate = get_currency_rate('USD')
 # MUST choose either .rial() or .toman()
 print(f"USD in Rials: {usd_rate.rial():,}")  
 print(f"USD in Tomans: {usd_rate.toman():,}")
 ```
 ### Getting Gold Rates
 ```python
 # Get 18k gold rate
 gold_18k = get_gold_rate(18)
 # MUST choose either .rial() or .toman()
 print(f"18k Gold per gram (Rials): {gold_18k.rial():,}")
 print(f"18k Gold per gram (Tomans): {gold_18k.toman():,}")
 ```
 ## Why You MUST Choose `.rial()` or `.toman()`
 In the Iranian currency system:
 - **Rial (﷼)** is the official currency
 - **Toman (تومان)** is an unofficial but widely used unit where:

   1 Toman = 10 Rials
 The conversion methods:
 - `.rial()` returns the raw value in Iranian Rials
 - `.toman()` converts the value to Tomans (dividing Rials by 10)
   
 You **must explicitly choose** between these methods because:
 1. Financial calculations require clear unit specification
 2. Automatic conversion could lead to dangerous financial errors
 3. Different use cases require different units (official vs common usage)
 4. Prevents ambiguity in financial reporting
 ## Error Handling
 The package raises custom exceptions for invalid inputs:
 ```
 try:
     # Attempt to get invalid currency
     get_currency_rate('XYZ')
 except InvalidCurrency as e:
     print(e)
 try:
     # Attempt to get invalid gold karat
     get_gold_rate(22)
 except InvalidMineral as e:
     print(e)
 ```
 ## Example Output
 ```
 USD in Rials: 500,530
 USD in Tomans: 50,053
 18k Gold per gram (Rials): 2,483,500
 18k Gold per gram (Tomans): 248,350
 ```

 ## Contributing
 Contributions are welcome! Please submit pull requests or open issues on [GitHub](https://github.com/MrMM7/tgju-api).
 ## License
 This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
 ## Disclaimer
 This package scrapes data from tgju.org. Use at your own risk. I The developers am not responsible for any financial decisions made using this data. Always verify rates with official sources before making transactions.
