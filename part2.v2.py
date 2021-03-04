# Welcome to Group 5 Interactive menu for your coin sorting

#first we will import the module sys
import sys

# then we delve into our script, considering the different options(1-5) analogous to the menu(1-5)

def option_1():
    print("***Coin calculator***")
    # insert single coin calculator here

    print("Welcome to Group 5 single denomination coin sorting program!")
    print("")
    print("Let's sort your coins for you")
    print("")
    print("Pick a coin from; 10p, 20p, 50p, 100p and 200p (given that 100 pennies = £1)")
    print("")
    print("We accept only pennies between 0 and 10,000p")
    print("")

    coins = [10, 20, 50, 100, 200]  #list of coins to select from
    ends = ["yes", "no"]
    
    pennies = int(input("Enter the coin denomination you want(between 10, 20, 50, 100 or 200): "))

# -----------------for the £2 ------------------------------------------------
    if pennies == 200 and pennies in coins: 
        print("You have chosen the 200p denomination")
        twohundredp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        
        if twohundredp < 0:
            print("Error, input value is not valid, try again!")
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

                

        elif twohundredp > 10000:
            print("Error, input value exceeded range, try again!")
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        else:
            two_hundred = twohundredp//200
            two_hundred_2 = two_hundred * 200
            two_hundred_remainder = (twohundredp - two_hundred_2)
            print("The number of £2 coins: " , int(two_hundred))
            print("Remainder: " , int(two_hundred_remainder) , "p")
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()
            

#-----------------for the £1   ----------------------------------------------
    elif pennies == 100 and pennies in coins:
        print("You have chosen the 100p denomination")
        onehundredp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        
        if onehundredp < 0:
            print("Error, input value is not valid, try again!")
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        elif onehundredp > 10000:
            print("Error, input value has exceeded range")  
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        else:
            one_hundred = onehundredp//100
            one_hundred_2 = one_hundred * 100
            one_hundred_remainder = (onehundredp - one_hundred_2)
            print("The number of £1 coins: " , int(one_hundred))
            print("Remainder: " , int(one_hundred_remainder) , "p")
            
            #user decides how to terminate
            ends = ["yes", "no"]
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

# ----------------------for 50p ----------------------------------------------
    elif pennies == 50 and pennies in coins:
        print("You have chosen the 50p denomination")
        fiftyp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        
        if fiftyp < 0:
            print("Error, input value is not valid value, try again!")
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        elif fiftyp > 10000:
            print("Error, input value exceeded range, try again!")   
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        else:
            fifty = fiftyp//50
            fifty_2 = fifty * 50
            fifty_remainder = (fiftyp - fifty_2)
            print("The number of 50p coins: " , int(fifty))
            print("Remainder: " , int(fifty_remainder) , "p")
            #user decides how to terminate
            ends = ["yes", "no"]
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

# ----------------- for 20p --------------------------------------------------
    elif pennies == 20 and pennies in coins:
        print("You have chosen the 20p denomination")
        twentyp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        
        if twentyp < 0:
            print("Error, input value is not valid, try again!")
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        elif twentyp > 10000:
            print("Error, input value exceeded range, try again!")   
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        else:
            twenty = twentyp//20
            twenty_2 = twenty * 20
            twenty_remainder = (twentyp - twenty_2)
            print("The number of 20p coins: " , int(twenty))
            print("Remainder: " , int(twenty_remainder) , "p")
            start_of_program()
             #user decides how to terminate
            ends = ["yes", "no"]
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

# ------------------ for 10p ------------------------------------------------
    elif pennies == 10 and pennies in coins:
        print("You have chosen the 10p denomination")
        tenp = int(input("Input how much money (in pennies) between 0 and 10000: "))
        
        if tenp <= 0:
            print("Error, input value is not valid, try again!")
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        elif tenp > 10000:
            print("Error, input value exceeded range, try again!")  
             #user decides how to terminate
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()

        else:
            ten = tenp//10
            ten_2 = ten * 10
            ten_remainder = (tenp - ten_2)
            print("The number of 10p coins: " , int(ten))
            print("Remainder: " , int(ten_remainder) , "p")
             #user decides how to terminate
            ends = ["yes", "no"]
            end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
            if end_call == "yes":
                start_of_program()
            elif end_call not in ends:
                print("Sorry wrong response")
                print("** Bye **")
            else:
                print("*** Bye ***")
                sys.exit()
                
# -------------------- if a wrong coin is entered -------------------------  
    else:
        print("Sorry, selected coin is not available")
        #user decides how to terminate
        ends = ["yes", "no"]
        end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
        if end_call == "yes":
            start_of_program()
        elif end_call not in ends:
            print("Sorry wrong response")
            print("** Bye **")
        else:
            print("*** Bye ***")
            sys.exit()


# ---- this is for menu 2 - multiple calculator ----------------------------- 

def option_2():
    print("***Multiple coin calculator***")
    # insert multiple coin calculator here
    coins = [10, 20, 50, 100, 200]
    ends = ["yes", "no"]
    print("")
    print("")
    print("Welcome to the multiple denominations coin sorter!")
    print("")
    print("You can input your pennies and sort it to get 10, 20, 50, £1 and £2")
    # list available denominators
    print("")
    print("You might also obtain a remainder (between 0 - 10p)")
    # clarify what the denominator value is
    print("")
    pennies = int(input("Input the amount of pennies to sort, between 0 and 10000: "))
    # give CONFIGURATION to user, stating that we are working in pennies and a valid range is given for the user to input into

    if pennies < 0 and pennies in coins:
        print("Error, input value is not valid, try again")
         #user decides how to terminate
        end_call = input("Enter 'yes' to Retry or 'no' to go back to Main Menu: ")
        if end_call == "yes":
            option_2()
        elif end_call not in ends:
            print("Sorry wrong response")
            sys.exit()
        else:
            start_of_program()

    elif pennies > 10000 and pennies in coins:
        print("Error, input value has exceeded range")       
    # give errors when the input is outside of the valid range 
    #user decides how to terminate
        end_call = input("Enter 'yes' to Retry or 'no' to go back to Main Menu: ")
        if end_call == "yes":
            option_2()
        elif end_call not in ends:
            print("Sorry wrong response")
            sys.exit()
        else:
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
            #user decides how to terminate
        end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
        if end_call == "yes":
            start_of_program()
        elif end_call not in ends:
            print("Sorry wrong response")
            print("** Bye **")
        else:
            print("*** Bye ***")
            sys.exit()
            



# ----------- this is for menu 3 (print coin list) ------------------------
def option_3():
    print("***Print Coin List***")
    print("The available denominators are 10p,20p, 50p, 100p and 200p (given in pennies e.g. 100 pennies = £1)")
    ends = ["yes", "no"]
    #user decides how to terminate
    end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
    if end_call == "yes":
        start_of_program()
    elif end_call not in ends:
        print("Sorry wrong response")
        print("** Bye **")
    else:
        print("*** Bye ***")
        sys.exit()



# -------------- this is for menu 4, which set details --------------------
def option_4():
    print("***Set Details Sub-Menu***")
    print("1 - Set currency")
    print("2 - Set minimum coin input value")
    print("3 - Set maximum coin input value")
    print("4 - Return to main menu")
    
    ends = ["yes", "no"]
    choice2 = int(input("Please choose an option here: "))

    if choice2 == 1:
        print("set currency here")
        currency_option = str(input("Please insert a currency (e.g GBP, USD,...): ")).upper()
        print("")
        print("You've selected {} as a currency to work with".format(currency_option))
        
        #user decides how to terminate
        end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
        if end_call == "yes":
            option_4()
        elif end_call not in ends:
            print("Sorry wrong response")
            print("** Bye **")
        else:
            print("*** Bye ***")
            sys.exit()
            

    elif choice2 == 2:
        print("set minimum coin value here")
        print("")
        min_coin = int(input("Enter the minimum coin you want (e.g 10 as 10p): "))
        print("")
        print("You've selected {} as your minimum coin".format(min_coin))
        
        #user decides how to terminate
        end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
        if end_call == "yes":
            option_4()
        elif end_call not in ends:
            print("Sorry wrong response")
            print("** Bye **")
        else:
            print("*** Bye ***")
            sys.exit()
            

    elif choice2 == 3:
        print("set maximum coin value here")
        print("")
        max_coin = int(input("Enter the maximum coin you want (e.g 200 as £2): "))
        print("")
        print("You've selected {} as your maximum coin".format(max_coin))
        
        #user decides how to terminate
        end_call = input("Enter 'yes' to perform another operation or 'no' to Exit: ")
        if end_call == "yes":
            option_4()
        elif end_call not in ends:
            print("Sorry wrong response")
            print("** Bye **")
        else:
            print("*** Bye ***")
            sys.exit()
            

    elif choice2 == 4:
      #this choice return the user to the main menu
      start_of_program()





def option_5():
    print("***Display program configurations***")
    # display config and return to menu
    
    start_of_program()






def option_6():
    print("")
    print("***Quitting the program***")
    print("*********** Bye **********")
    sys.exit()






def start_of_program():
    print("***Coin Sorter - Main Menu***")
    print("1 - Coin calculator")
    print("2 - Multiple coin calculator")
    print("3 - Print coin list")
    print("4 - Set details")
    print("5 - Display program configurations")
    print("6 - Quit the program")
    choice = int(input("Please choose an operation: "))

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
        print("Wrong input, try again!")
        print("")
        start_of_program()
        print("")

        

start_of_program()
