

#-------- Phone book ------

dict1 = {
    'Amal':1111111111,
    'Mohammed':2222222222,
    'Khadijah': 3333333333,
    'Abdullah':4444444444,
    'Rawan': 5555555555,
    'Faisal': 6666666666,
    'Layla' : 7777777777
}

#-------------- 1 and 2 and 3 ---------------
specific = '!@#$%^&*()_-+={}[]'
i = input("Enter number: ")
if len(i) == 10:
    for x in dict1:
        if dict1[x] == int(i):
            print(x)
            break


else:
    print("This is invalid number")








