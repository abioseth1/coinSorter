#Currency Converter - Group 5

import json, urllib.request


#See full lists of valid currencies on https://www.alphavantage.co/documentation

#Display banner
print("$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€")
print("$£¥€                            $£¥€")
print("$£¥€ Group 5 Currency Converter $£¥€")
print("$£¥€                            $£¥€")
print("$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€$£¥€")
print("")
print("Examples of currencies,(you also input any other minor currency of your choice): ")
print("  GBP - British Pound £")
print("  MGA - Malagasy Ariary Ar")
print("  USD - US Dollar $")
print("  EUR - Euro €")
print("  JPY - Japanese Yen ¥")
print("")

# Using Alpha Vantage API
api_key = "92REN3HWQYJGNQFD"

#Initialise key variables
currencyFrom = ""
currencyTo = ""
amount = 0

#Retrieve user inputs
#while currencyFrom.isalpha():
currencyFrom = input("Enter Currency to convert From (e.g. GBP): ").upper()
  
#while currencyTo.isalpha():
currencyTo = input("Enter Currency to convert To (e.g. EUR): ").upper()

amount = float(input("Enter amount to convert (e.g. 50): "))

#A JSON request to retrieve the required exchange rate

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + currencyFrom + '&to_currency=' + currencyTo + '&apikey=' + api_key

response = urllib.request.urlopen(main_url)
result = json.loads(response.read())
   
#Let's extract the required information
exchangeRate = result['Realtime Currency Exchange Rate']
rate = exchangeRate['5. Exchange Rate']

#Output exchange rate and converted amount
print('Realtime exchange rate')
print(f'1 {currencyFrom} : {rate} {currencyTo}')
print('Converted amount')
print(f'{amount} {currencyFrom} : {float(rate) * amount} {currencyTo}')
