from termcolor import colored # To add colored to printed messages :) <3

# Define a dict that hold owners and there phone numbers
phone_book_dict = {
    'Amal': '1111111111',
    'Mohammed': '2222222222',
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Rawan': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}

# Function To check if the entered numbe contains any letters or symbols
def check_phone_number(phone_number):
    symbols_flag = False 
    letters_flag = False
    for i in phone_number:
        if i in "!@#$%^&*()+=-_[]?><,.:":
            symbols_flag=True
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            letters_flag=True
        
    return symbols_flag and letters_flag

# Function to add new recored to dictionary 
def add_phone(phone_num):
    print()
    print("-------------------------------------------------------")
    print(colored("To add the phone number please provid a name",'yellow'))
    user_name = input("| Please Enter a name: ")
    phone_book_dict[user_name] = phone_num
    print(colored("The recored added successfully","green"))
    print("-------------------------------------------------------")

# Function To search the owner of the number
def found_owner(phone):
    found = False
    for name,number in phone_book_dict.items():
        if number == phone:
            print(colored("There is one phone number that matches","green"))
            print("-------------------------------------------------------")
            print("The owner is: ", name)
            print("The phone number is: ", number)
            print("-------------------------------------------------------")
            print("Back to main .....")
            found = True
    if not found:
        print(colored("% Sorry, the number is not found %","red"))
        answer = input("Whould you like to add this number to the phone book? [y/n]")
        while True:
            if answer == 'y' or answer =='Y':
                add_phone(phone)
                break
            if answer == 'n' or answer == 'N':
                print("Back to main .....")
                break
            else:
                print(colored("% Sorry, invalid input try again%","red"))
                answer = input("Whould you like to add this number to the phone book? [y/n]")
                

'''
----------------------------- START of Program -----------------------------
'''
# Loop to keep ask user unti he/she quit:
while True:
    print()
    print("-------------------------------------------------------")
    print("-------- Welcome To Phone Number Owner Founder --------")
    print("-------------------------------------------------------")
    print()
    #Take the number form the user:
    user_input = input('| Please enter a valid phone number (q to quit): ')
    if user_input == 'q' or user_input =='Q':
        break
    else:
        #Validate user input phone
        while len(user_input) !=10 or check_phone_number(user_input):
            print(colored("% This is invalid number %","red"))
            user_input = input('| Please enter again: ')
        found_owner(user_input)


