phone_book={
"Amal":"1111111111",
"Mohammed":"2222222222",
"Khadijah":"3333333333",
"Abdullah":"4444444444" ,
"Rawan" :"5555555555",
"Faisal" :"6666666666",
"Layla" : "7777777777"
}

x=input("Hello \n Can you enter phone number: ")


for key, value in phone_book.items():
    if x == value:
        print("The owner is " + key)
        break

if len(x) >10 or len(x)<10:
    print("This is invalid number")

elif x.isdigit() == False:
    print("This is invalid number")

elif x != value:
    print("Sorry, the number is not found")



























