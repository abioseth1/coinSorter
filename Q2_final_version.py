# Welcome to Group 5 code for your coin sorting program
# Below, we have inported a library and defined the default currency, min + max inputs unless they have been edited while running
import sys
currency_1 = "p"
min_input = 0
max_input = 10000

# We have defined each option from the main menu as a diferent function to keep the code organised
# The code breaks down all of the options (1-6), before defining the main menu at the bottom of the code

# Here, we introduce the coin sorting program and ask for a coin denomination and an input coin value to be sorted
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
    # pennies is a variable that the user will decide as the chosen coin denominator, below are the different coding for the different options given as if, elif statements. The input must be an integer. I used this in my favour to define a integer to go back to the main menu (0)   
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
    # each code block has the same layout, it says if the user inputs that given coin denomination (200,100,50,20,10), then they are asked to define a coin value. This value must fall within the range defined by the user. 
    # The program takes the input coin value, divides it by the denominator and gives the remainder as a chosen currency. After the calculation, the user is taken to the start of the sub-menu where they can quit or do another calculation
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






# option 2 leads the user to the multiple coin denomination, where an input value given (between a defined input range) is sorted into all the available denominators (10,20,50,100,200)
# the output is printed below. There is alos an option to input 0 (similar to option 1) to return to the main menu
# the modulus function % was used to denonate the denominatons, with the remainder calculated too.
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
    # ranges defined - must be between min and max output
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
    # every number input between the defined range will be sorted into the denominators
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







# This option defines for the user the denominations that are available. The list is printed and then the user returns to the main menu.
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





# This option allows the user to enter a sub-menu to set the program configuration
# the variables that hold the inputted configurations are global, which mean they are saved to the program and override any other value of the variable previously stated.
# The menu printed below gives options to change given parameters or return to the main menu
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
    choice2 = int(input("Please choose an option here by selecting one of the numbers (1-4): "))
    print("")
    # A given input here will define the UNIT of currency that the user wishes to use. The currencies are number corresponding. After an input is given, the variable is stored and the user is returned to the sub menu.
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

    # The two options below represent a chance for the user to input a given range for all coin denomination calculations. After an input is given, the variables are stored and the user is returned to the sub menu.
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

# choices for currency are p and £ , cent and $, malagasey airey
# the given range can be defined as any value.





# This option when called upon will print the current configurations of the program including the currency and boundary inputs. After doing this, the user is redirected to the main menu
# Since these variables are functions, they will print the current configuration that was defined in option 5. If nothing is defined, the default currency and limits are ued, defined at the start of the program.
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







# option 6 uses a function imported from the sys libary to quit the program and stop the program after a message is displayed
def option_6():
    print("")
    print("")
    print("***Quitting the program...***")
    sys.exit()








# Below gives the structure to the main menu, this is the first thing to be printed as start_of_program() is given at the bottom of the code.
# When a defined number as explained in the print below is chosen, the user will be redirected to that option
# This is done by if/elif statements that lead to the other functions being called upon. If an invalid number is given, the user is redirected to the main menu.
def start_of_program():
    print("***Coin Sorter - Main Menu***")
    print("1 - Coin calculator")
    print("2 - Multiple coin calculator")
    print("3 - Print coin list")
    print("4 - Set details")
    print("5 - Display program configurations")
    print("6 - Quit the program")
    choice = int(input("Please choose an option here by selecting one of the numbers (1-6): "))

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
    else:
        
        print("")
        print("Invalid option")
        print("")
        print("Returning to the main menu...")
        print("")
        print("")
        start_of_program()


        
# Here, we define that the first thing that is called is the start_of_program() function. 
# Since this piece of coding is not in a function, this line is the first point of action for the system.
start_of_program()
