import sys
currency_1 = "p"
min_input = 0
max_input = 10000

def option_1():
    print("")
    print("")
    print("Welcome to the coin sorting program!")
    print("")
    print("In this program, we will sort out a coin value in pennies/cents/malagasy ariarys into a chosen demoninator with a remainder!")
    print("")
    print("The available denominators are 10, 20, 50, 100 and 200")
    print("")
    print("The input value range is set between 0 - 10,000 unless stated otherwise. Any value given outside of this range will result in returning to the sub menu.")
    print("")
    print("Alternatively, you can type 0 to return to the main menu" )
    print("")
    pennies = int(input( "Which coin sorting denominatior would you like to choose from? (choose between 0, 10, 20, 50, 100 or 200) : " ))
        
    if pennies == 200: 
        print("")
        print("You have chosen the 200 denominator")
        print("")
        twohundredp = int(input("Input how much money to be sorted: "))
        if twohundredp < min_input:
            print("Error, input value is not a valid value")
            option_1()

        elif twohundredp > max_input:
            print("Error, input value has exceeded range")   
            option_1()

        else:
            two_hundred = twohundredp//200
            two_hundred_2 = two_hundred * 200
            two_hundred_remainder = (twohundredp - two_hundred_2)
            print("The number of 200" ,currency_1,  "coins: "  , int(two_hundred))
            print("Remainder: " , int(two_hundred_remainder) , currency_1)
        option_1()


    elif pennies == 100:
        print("")
        print("You have chosen the 100 denominator")
        print("")
        onehundredp = int(input("Input how much money to be sorted: "))
        if onehundredp < min_input:
            print("Error, input value is not a valid value")
            option_1()

        elif onehundredp > max_input:
            print("Error, input value has exceeded range")  
            option_1() 

        else:
            one_hundred = onehundredp//100
            one_hundred_2 = one_hundred * 100
            one_hundred_remainder = (onehundredp - one_hundred_2)
            print("The number of 100" , currency_1,  "coins: " , int(one_hundred))
            print("Remainder: " , int(one_hundred_remainder) , currency_1)
        option_1()


    elif pennies == 50:
        print("")
        print("You have chosen the 50 denominator")
        print("")
        fiftyp = int(input("Input how much money to be sorted: "))
        if fiftyp < min_input:
            print("Error, input value is not a valid value")
            option_1()

        elif fiftyp > max_input:
            print("Error, input value has exceeded range") 
            option_1()  

        else:
            fifty = fiftyp//50
            fifty_2 = fifty * 50
            fifty_remainder = (fiftyp - fifty_2)
            print("The number of 50" , currency_1 ,  "coins: " , int(fifty))
            print("Remainder: " , int(fifty_remainder) , currency_1)
        option_1()


    elif pennies == 20:
        print("")
        print("You have chosen the 20 denominator")
        print("")
        twentyp = int(input("Input how much money to be sorted: "))
        if twentyp < min_input:
            print("Error, input value is not a valid value")
            option_1()

        elif twentyp > max_input:
            print("Error, input value has exceeded range")  
            option_1() 

        else:
            twenty = twentyp//20
            twenty_2 = twenty * 20
            twenty_remainder = (twentyp - twenty_2)
            print("The number of 20" , currency_1 ,  "coins: " , int(twenty))
            print("Remainder: " , int(twenty_remainder) , currency_1)
        option_1()
       

    elif pennies == 10:
        print("")
        print("You have chosen the 10 denominator")
        print("")
        tenp = int(input("Input how much money to be sorted: "))
        if tenp < min_input:
            print("Error, input value is not a valid value")
            option_1()

        elif tenp > max_input:
            print("Error, input value has exceeded range")   
            option_1()

        else:
            ten = tenp//10
            ten_2 = ten * 10
            ten_remainder = (tenp - ten_2)
            print("The number of 10" , currency_1,  "coins: " , int(ten))
            print("Remainder: " , int(ten_remainder) , currency_1)
        option_1()

    elif pennies == 0: 
        print("")
        print("")
        print("***Returning to Main Menu...***")
        print("")
        print("")
        start_of_program()
    else:
        print("You have selected an invalid denominator. Returning to the sub-menu...")
        option_1()








def option_2():
    print("")
    print("")
    print("Welcome to the multiple denominator coin sorter!")
    print("")
    print("You can input a coin value below and the program will sort the coins in terms of 10, 20, 50, 100 and 200p")
    print("")
    print("The input must be between 0 - 10,000 unless stated otherwise. Any value given outside of this range will result in returning to the sub menu.")
    print("")
    print("The program can calculate a remainder of any coins that were not sorted (will be between 0 - 10p)")
    print("")
    print("Alternatively, you can type 0 to return to the main menu" )
    print("")
    pennies = int(input("Input how much money to be sorted, or input 0 to return to the main menu: "))

    if pennies < min_input:
        print("")
        print("Error, input value is not a valid value")
        print("")
        print("Reurning to the start of the sub-menu...")
        print("")
        option_2()

    elif pennies > max_input:
        print("")
        print("Error, input value is not a valid value")
        print("")
        print("Reurning to the start of the sub-menu...")
        print("")
        option_2()

    elif pennies == 0:
        print("") 
        print("***Returning to the Home Screen***")  
        print("") 
        print("")   
        print("")   
        start_of_program()  

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

        #five = (pennies % 200 % 100 % 50 % 20 % 10 ) // 5
        #two = (pennies % 200 % 100 % 50 % 20 % 10 % 5 ) // 2
        #one = (pennies % 200 % 100 % 50 % 20 % 10 % 5 % 2 ) // 1

        print("The number of 200" , currency_1,  "coins: " , int(two_hundred)) 
        print("The number of 100" , currency_1,  "coins: " , int(one_hundred))
        print("The number of 50" , currency_1, "coins: " , int(fifty))
        print("The number of 20" , currency_1, "coins: " , int(twenty))
        print("The number of 10" ,currency_1, "coins: " , int(ten))
        print("The remainder: " , int(remainder) , currency_1)
        print("")
        print("")
        option_2()








def option_3():
    print("")
    print("")
    print("***Print Coin List***")
    print("")
    print("The available denominators are 10, 20, 50, 100 and 200")
    print("")
    print("***Returning to the start of the program...***")
    print("")
    print("")
    start_of_program()








def option_4():
    global currency_1
    global min_input
    global max_input
    print("")
    print("")
    print("***Set Details Sub-Menu***")
    print("1 - Set currency")
    print("2 - Set minimum coin input value")
    print("3 - Set maximum coin input value")
    print("4 - Return to main menu")
    choice2 = int(input("Please choose an option here: "))
    print("")
    
    if choice2 == 1:
        print("")
        print("Choose between GDP (£), USD ($) and MGA (Malagasy Ariary Ar)")
        print("")
        currency = int(input("Input 1 for GDP (£), 2 for USD ($) and 3 for MGA (Malagasy Ariary Ar): "))
        print("")
        if currency == 1:
            print("You have selected GDP as your chosen currency")
            currency_1 = "p"
            

            option_4()
        elif currency == 2:
            print("You have selected USD as your chosen currency")
            currency_1 = "cent(s)"

            option_4()
        elif currency == 3:
            print("You have selected MGA as your chosen currency")
            currency_1 = "malagasey airey"

            option_4()
        else:
            print("You have inputted an invalid currency")
            option_4()

    
    elif choice2 == 2:
        print("")
        min_input = int(input("Input the minimum coin value: "))
        print("")
        print("You have chosen" , min_input , "as your input value" )
        option_4()


    
    elif choice2 == 3:
        print("")
        max_input = int(input("Input the maximum coin value: "))
        print("")
        print("You have chosen" , max_input , "as your input value" )
        option_4()
    
    elif choice2 == 4:
        print("***Returning to the Main Menu...***")
        print("")
        print("")
        start_of_program()

# choices are p and £ , cent and $, malagasey airey







def option_5():
    print("")
    print("")
    print("***Display program configurations***")
    print("")
    print("The current currency setting is:" , currency_1 )
    print(" p = pennies (GDP) , cent(s) = cents (USD) , malagasey airey (MGA) ")
    print("")
    print("The minimum coin input value is: " , min_input)
    print("")
    print("The maximum coin input value is: " , max_input)
    print("")
    print("")
    start_of_program()








def option_6():
    print("")
    print("")
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

