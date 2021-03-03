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

