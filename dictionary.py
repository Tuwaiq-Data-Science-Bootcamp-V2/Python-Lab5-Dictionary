phone_book={
"Amal":"1111111111",
"Mohammed":"2222222222",
"Khadijah":"3333333333",
"Abdullah":"4444444444" ,
"Rawan" :"5555555555",
"Faisal" :"6666666666",
"Layla" : "7777777777"
}

x=input("Enter Phone Number: ")


for key, value in phone_book.items():
  if x == value:
      print(key)



def num():
    if len(x) > 10 or len(x) < 10:
        print("This is invalid number")

    elif x.isdigit():
        print("This is invalid number")
num()



























