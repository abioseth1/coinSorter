import sys

def option_1():
    print("")
    print("")
    print("Welcome to the coin sorting program!")
    print("")
    print("In this program, we will sort out a coin value into a chosen demoninator with a remainder!")
    print("")
    print("The available denominators are 10, 20, 50, 100 and 200 (given in pennies e.g. 100 pennies = £1)")
    print("")
    print("The input value for sorting in pennies is limited between 0 and 10,000p")
    print("")
    print("Alternatively, you can type 0 to return to the main menu" )
    print("")
    pennies = int(input( "Which coin sorting denominatior would you like to choose from? (choose between 0, 10, 20, 50, 100 or 200) : " ))
        
    if pennies == 200: 
        print("")
        print("You have chosen the 200p denominator")
        print("")
        twohundredp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if twohundredp <= 0:
            print("Error, input value is not a valid value")

        elif twohundredp >= 10000:
            print("Error, input value has exceeded range")   

        else:
            two_hundred = twohundredp//200
            two_hundred_2 = two_hundred * 200
            two_hundred_remainder = (twohundredp - two_hundred_2)
            print("The number of £2 coins: " , int(two_hundred))
            print("Remainder: " , int(two_hundred_remainder) , "p")
        option_1()


    elif pennies == 100:
        print("")
        print("You have chosen the 100p denominator")
        print("")
        onehundredp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if onehundredp <= 0:
            print("Error, input value is not a valid value")

        elif onehundredp >= 10000:
            print("Error, input value has exceeded range")   

        else:
            one_hundred = onehundredp//100
            one_hundred_2 = one_hundred * 100
            one_hundred_remainder = (onehundredp - one_hundred_2)
            print("The number of £1 coins: " , int(one_hundred))
            print("Remainder: " , int(one_hundred_remainder) , "p")
        option_1()


    elif pennies == 50:
        print("")
        print("You have chosen the 50p denominator")
        print("")
        fiftyp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if fiftyp <= 0:
            print("Error, input value is not a valid value")

        elif fiftyp >= 10000:
            print("Error, input value has exceeded range")   

        else:
            fifty = fiftyp//50
            fifty_2 = fifty * 50
            fifty_remainder = (fiftyp - fifty_2)
            print("The number of 50p coins: " , int(fifty))
            print("Remainder: " , int(fifty_remainder) , "p")
        option_1()


    elif pennies == 20:
        print("")
        print("You have chosen the 20p denominator")
        print("")
        twentyp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if twentyp <= 0:
            print("Error, input value is not a valid value")

        elif twentyp >= 10000:
            print("Error, input value has exceeded range")   

        else:
            twenty = twentyp//20
            twenty_2 = twenty * 20
            twenty_remainder = (twentyp - twenty_2)
            print("The number of 20p coins: " , int(twenty))
            print("Remainder: " , int(twenty_remainder) , "p")
        option_1()
       

    elif pennies == 10:
        print("")
        print("You have chosen the 10p denominator")
        print("")
        tenp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        if tenp <= 0:
            print("Error, input value is not a valid value")

        elif tenp >= 10000:
            print("Error, input value has exceeded range")   

        else:
            ten = tenp//10
            ten_2 = ten * 10
            ten_remainder = (tenp - ten_2)
            print("The number of 10p coins: " , int(ten))
            print("Remainder: " , int(ten_remainder) , "p")
        option_1()

    if pennies == 0: 
        print("")
        print("")
        print("***Returning to Main Menu...***")
        print("")
        print("")
        start_of_program()







def option_2():
    print("***Multiple coin calculator***")
    # insert multiple coin calculator here





def option_3():
    print("")
    print("")
    print("***Print Coin List***")
    print("")
    print("The available denominators are 10, 20, 50, 100 and 200 (given in pennies e.g. 100 pennies = £1)")
    print("")
    print("***Returning to the start of the program...***")
    print("")
    print("")
    start_of_program()




def option_4():
    print("")
    print("")
    print("***Set Details Sub-Menu***")
    print("1 - Set currency")
    print("2 - Set minimum coin input value")
    print("3 - Set maximum coin input value")
    print("4 - Return to main menu")
    choice2 = int(input("Please choose an option here: "))
    if choice2 == 1:
        print("set currency here")
    elif choice2 == 2:
        print("set minimum coin value here")
    elif choice2 == 3:
        print("set maximum coin value here")
    elif choice2 == 4:
        print("***Returning to the Main Menu...***")
        print("")
        print("")
        start_of_program()





def option_5():
    print("***Display program configurations***")
    # display config and return to menu






def option_6():
    print("***Quitting the program...***")
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

