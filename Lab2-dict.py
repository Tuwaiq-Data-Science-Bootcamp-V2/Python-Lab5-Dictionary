#phone book dictionary
phone_book ={
   	'1111111111' : "Amal",
	'2222222222' : "Mohammed",
	'3333333333' : "Khadija",
	'4444444444' : "Abdullah",
	'5555555555' : "Rawan",
	'6666666666' : "Faisal",
	'7777777777' : "Layla"
}
#input from user
phone_num = input("Enter phone number :")

#check if the number in the dictionary
if phone_num in phone_book:
    print(phone_book[phone_num])

#invalidtion masseges
if len(phone_num)!=10:
    print("This is invalid number")
for i in phone_num:
    if i not in ("0987654321"):
        print("This is invalid number")
        break


    
    

      
