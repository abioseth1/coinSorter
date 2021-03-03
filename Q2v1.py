import sys

def option_1():
    print("***Coin calculator***")
    # insert single coin calculator here



def option_2():
    print("***Multiple coin calculator***")
    # insert multiple coin calculator here



def option_3():
    print("***Print Coin List***")
    print("The available denominators are 10, 20, 50, 100 and 200 (given in pennies e.g. 100 pennies = £1)")
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
    elif choice2 == 2:
        print("set minimum coin value here")
    elif choice2 == 3:
        print("set maximum coin value here")
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

