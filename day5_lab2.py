PhoneBook = { "Amal":1111111111 ,"Mohammed":2222222222 , "Khadijah":3333333333 , "Abdullah": 4444444444, "Rawan": 5555555555 , "Faisal":6666666666, "Layla":7777777777}
number = input("Enter phone number")
def Phone_Book():
    #or use isinstance()
    if len(number) != 10 or number.isnumeric() != True :
        print("This is invalid number")
        
    else:
        for i in PhoneBook:
             if number == PhoneBook.values():
                print(PhoneBook.keys())
             else:
                print("Sorry, the number is not found")

    
Phone_Book()