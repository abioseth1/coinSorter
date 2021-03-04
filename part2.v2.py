def option_1():
    print("***Coin calculator***")
    # insert single coin calculator here

    print("Welcome to Group 5 single denomination coin sorting program!")
    print("")
    print("In this program, we will sort your coins into a chosen demonination and possibly give a remainder!")
    print("")
    print("The available denominations are 10p, 20p, 50p, 100p and 200p (given that 100 pennies = Â£1)")
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
            print("The number of Â£2 coins: " , int(two_hundred))
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
            print("The number of Â£1 coins: " , int(one_hundred))
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

            option_1()




def option_2():
    print("***Multiple coin calculator***")
    # insert multiple coin calculator here
    
    print("")
    print("")
    print("Welcome to the multiple denominations coin sorter!")
    print("")
    print("You can input a coin value below and the program will sort the coins in terms of 10, 20, 50, 100 and 200p")
    # list available denominators
    print("")
    print("The program can calculate a remainder of any coins that were not sorted (will be between 0 - 10p)")
    # clarify what the denominator value is
    print("")
    pennies = int(input("Input how much money that you would like to sort (in pennies) between 0 and 10000: "))
    # give CONFIGURATION to user, stating that we are working in pennies and a valid range is given for the user to input into

    if pennies <= 0:
        print("Error, input value is not a valid value")

    elif pennies >= 10000:
        print("Error, input value has exceeded range")       
    # give errors when the input is outside of the valid range 
    else:
        two_hundred = pennies//200
        two_hundred2 = two_hundred * 200
        one_hundred = (pennies % 200) // 100
        one_hundred2 = one_hundred * 100
        fifty = (pennies % 200 % 100) // 50
        fifty2 = fifty * 50
        twenty = (pennies % 200 % 100 % 50) // 20
        twenty2 = twenty * 20
        ten = (pennies % 200 % 100 % 50 % 20) // 10
        ten2 = ten * 10
        remainder =  (pennies - two_hundred2 - one_hundred2 - fifty2 - twenty2 - ten2)
     # calculations to show hwo the coin sorting process is completed
        #five = (pennies % 200 % 100 % 50 % 20 % 10 ) // 5
        #two = (pennies % 200 % 100 % 50 % 20 % 10 % 5 ) // 2
        #one = (pennies % 200 % 100 % 50 % 20 % 10 % 5 % 2 ) // 1

        print("The number of £2 coins: " , int(two_hundred)) 
        print("The number of £1 coins: " , int(one_hundred))
        print("The number of 50p coins: " , int(fifty))
        print("The number of 20p coins: " , int(twenty))
        print("The number of 10p coins: " , int(ten))
        print("The remainder: " , int(remainder) , "p")



def option_3():
    print("***Print Coin List***")
    print("The available denominators are 10p,20p, 50p, 100p and 200p (given in pennies e.g. 100 pennies = Â£1)")
    start_of_program()




def option_4():
    print("***Set Details Sub-Menu***")
    print("1 - Set currency")
    print("2 - Set minimum coin input value")
    print("3 - Set maximum coin input value")
    print("4 - Return to main menu")
    choice2 = int(input("Please choose an option here: "))

    if choice2 == 1:
        print("set currency here")
        currency_option = str(input("Please insert a currency (e.g GBP, USD,...): ")).upper()
        option_4()

    elif choice2 == 2:
        print("set minimum coin value here")
        print("")
        print(int(input("Enter the minimum no. of coins you like to work with (min of zero)")))
        option_4()

    elif choice2 == 3:
        print("set maximum coin value here")
        print("")
        print(int(input("Enter the maximum  no. of coins you want to work with(up to 100000)")))
        option_4()

    elif choice2 == 4:
      start_of_program()





def option_5():
    print("***Display program configurations***")
    # display config and return to menu






def option_6():
    print("***Quit the program***")
    sys.exit()






def start_of_program():
    print("***Coin Sorter - Main Menu***")
    print("1 - Coin calculator")
    print("2 - Multiple coin calculator")
    print("3 - Print coin list")
    print("4 - Set details")
    print("5 - Display program configurations")
    print("6 - Quit the program")
    choice = int(input("Please choose an option here: "))

    if choice == 1:
        option_1()

    elif choice == 2:
        option_2()

    elif choice == 3:
        option_3()
        
    elif choice == 4:
        option_4()

    elif choice == 5:
        option_5()

    elif choice == 6:
        option_6()

        

start_of_program()