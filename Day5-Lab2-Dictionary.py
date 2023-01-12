# Phonebook
phone_book = {1111111111: 'Amal', 2222222222: 'Mohammed', 3333333333: 'Khadijah', 4444444444: 'Abdullah',
              5555555555: 'Rawan', 6666666666: 'Faisal', 7777777777: 'Layla'}

while True:
    # Enter the number
    phone_num = (input('Enter the phone number\n'))
    # Check if the number format is correct
    if phone_num.isdigit():
        phone_num = int(phone_num)
        if 999999999 < phone_num < 10000000000:
            break
        else:
            print('This is invalid number')
    else:
        print('Enter number only')

# Check id the number is in the phonebook
if phone_num in phone_book:
    print('the owner of the number {} is {} '.format(phone_num, phone_book[phone_num]))
else:
    print('Sorry, the number is not found')
