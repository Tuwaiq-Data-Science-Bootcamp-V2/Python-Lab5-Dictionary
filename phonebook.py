phonebook = {"numbers": {
    "names_and_numbers": [
        {"number": 1111111111,
         "name": "amal"
         },
        {"number": 2222222222,
         "name": "Mohammed"
         },
        {"number": 3333333333,
         "name": "Khadijah"
         },
        {"number": 4444444444,
         "name": "Abdullah"
         },
        {"number": 5555555555,
         "name": "Rawan"
         },
        {"number": 6666666666,
         "name": "Faisal"
         },
        {"number": 7777777777,
         "name": "Layla"
         }
    ]
}
}

number = int(input("What's is the number ? "))
while (len(str(number))) != 10:
    print("Sorry, the number is not found ")
    number = int(input("What's is the number ? "))
else:
    print("Valid number")

for n in phonebook['numbers']['names_and_numbers']:
    if n.get('number') == number:
        print('The owner of this number {} is {}'.format(n.get("number"), n.get("name")))
