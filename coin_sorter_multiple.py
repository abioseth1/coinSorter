print("Welcome to the multiple denominator coin sorter!")
print("You can input a coin value below and the program will sort the coins in terms of 10, 20, 50, 100 and 200p")
print("The program can calculate a remainder of any coins that were not sorted (will be between 0 - 10p)")
pennies = int(input("Input how much money (in pennies) between 0 and 10000: "))

if pennies <= 0:
        print("Error, input value is not a valid value")

elif pennies >= 10000:
        print("Error, input value has exceeded range")       

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

        print("The number of £2 coins: " , int(two_hundred)) 
        print("The number of £1 coins: " , int(one_hundred))
        print("The number of 50p coins: " , int(fifty))
        print("The number of 20p coins: " , int(twenty))
        print("The number of 10p coins: " , int(ten))
        print("The remainder: " , int(remainder) , "p")



