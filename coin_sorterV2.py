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

        print("There are" , int(two_hundred) , "£2 coins")
        print("There are" , int(one_hundred) , "£1 coins")
        print("There are" , int(fifty) , "50p coins")
        print("There are" , int(twenty) , "20p coins")
        print("There are" , int(ten) , "10p coins")
        print("There are" , int(remainder) , "pennies as a remainder")
