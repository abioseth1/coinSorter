print("Welcome to Group 5 Currency Program!")
print("")
print(" You can either Sort your pennies into desirable denominations \
or perform exchange rate conversion of one currency to another  ")
print("")

choice = int(input(" Enter 1 for Coin Sorter or 2 for Currency Conversion"))

if choice == 1:
    
    print("Welcome to Group 5 coin sorting program!")
    print("")
    print("In this program, we will sort your coins into a chosen demonination and possibly give a remainder!")
    print("")
    print("The available denominations are 10p, 20p, 50p, 100p and 200p (given that 100 pennies = £1)")
    print("")
    print("The input value for sorting in pennies is limited between 0 and 10,000p")
    print("")

    pennies = int(input("Which coin sorting denomination would you like to choose from? (choose between 10, 20, 50, 100 or 200): "))

    if pennies == 200: 
        print("You have chosen the 200p denomination")
        twohundredp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if twohundredp <= 0:
            print("Error, input value is not valid, try again!")

        elif twohundredp >= 10000:
            print("Error, input value exceeded range, try again!")   

        else:
            two_hundred = twohundredp//200
            two_hundred_2 = two_hundred * 200
            two_hundred_remainder = (twohundredp - two_hundred_2)
            print("The number of £2 coins: " , int(two_hundred))
            print("Remainder: " , int(two_hundred_remainder) , "p")


    elif pennies == 100:
        print("You have chosen the 100p denomination")
        onehundredp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if onehundredp <= 0:
            print("Error, input value is not valid, try again!")

        elif onehundredp >= 10000:
            print("Error, input value has exceeded range")   

        else:
            one_hundred = onehundredp//100
            one_hundred_2 = one_hundred * 100
            one_hundred_remainder = (onehundredp - one_hundred_2)
            print("The number of £1 coins: " , int(one_hundred))
            print("Remainder: " , int(one_hundred_remainder) , "p")


    elif pennies == 50:
        print("You have chosen the 50p denomination")
        fiftyp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if fiftyp <= 0:
            print("Error, input value is not valid value, try again!")

        elif fiftyp >= 10000:
            print("Error, input value exceeded range, try again!")   

        else:
            fifty = fiftyp//50
            fifty_2 = fifty * 50
            fifty_remainder = (fiftyp - fifty_2)
            print("The number of 50p coins: " , int(fifty))
            print("Remainder: " , int(fifty_remainder) , "p")


    elif pennies == 20:
        print("You have chosen the 20p denomination")
        twentyp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if twentyp <= 0:
            print("Error, input value is not valid, try again!")

        elif twentyp >= 10000:
            print("Error, input value exceeded range, try again!")   

        else:
            twenty = twentyp//20
            twenty_2 = twenty * 20
            twenty_remainder = (twentyp - twenty_2)
            print("The number of 20p coins: " , int(twenty))
            print("Remainder: " , int(twenty_remainder) , "p")


    elif pennies == 10:
        print("You have chosen the 10p denomination")
        tenp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if tenp <= 0:
            print("Error, input value is not valid, try again!")

        elif tenp >= 10000:
            print("Error, input value exceeded range, try again!")   

        else:
            ten = tenp//10
            ten_2 = ten * 10
            ten_remainder = (tenp - ten_2)
            print("The number of 10p coins: " , int(ten))
            print("Remainder: " , int(ten_remainder) , "p")




if choice == 2:

    #Currency Converter 

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
    currencyFrom = input("Enter Currency to convert From: (e.g. GBP)").upper()

    #while currencyTo.isalpha():
    currencyTo = input("Enter Currency to convert To: (e.g. EUR)").upper()

    amount = float(input("Enter amount to convert: (e.g. 50)"))

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
