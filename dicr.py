phoneBook = {
'1111111111':"Amal",
'2222222222':"Mohammed",
'3333333333':"Khadija",
'4444444444':"Abdullah",
'5555555555':"Rawan",
'6666666666':"Faisal",
'7777777777':"Layla"}
while True:
    phoneNum = input("If you want check if the Number in the Phone book Please write the number: ")
    if phoneNum in phoneBook:
        print("Yes it's", phoneBook[phoneNum])
    elif len(phoneNum)!=10:
        print("This is invalid number, please check again")
    for i in phoneNum:
        if i not in ("0987654321"):
            print("This is invalid, please check again")


