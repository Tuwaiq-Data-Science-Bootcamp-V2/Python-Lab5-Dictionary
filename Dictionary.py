#!/usr/bin/env python
# coding: utf-8

# In[4]:


dict = { '1' : {'Name': 'Amal',     'Number': 1111111111 },
         '2' : {'Name': 'Mohammed', 'Number': 2222222222 },
         '3' : {'Name': 'Khadijah', 'Number': 3333333333 },
         '4' : {'Name': 'Abdullah', 'Number': 4444444444 },
         '5' : {'Name': 'Rawan',    'Number': 5555555555 },
         '6' : {'Name': 'Faisal',   'Number': 6666666666 },
         '7' : {'Name': 'Layla',    'Number': 7777777777 }}

print(dict)


# In[7]:


Number = input("Enter the number: ")
if len(Number)>10 or len(Number)<10:
    print("This is invalid number")
elif not Number.isnumeric():
    print("This is invalid number, the number has letters")
else:
    not_found= True
    for key,value in dict.items():
        if int(Number) == value["Number"]:
            print("Owner is:", value["Name"])
            not_found = False
            break
    if not_found:
            print("Sorry, the number is not found")


# In[ ]:





# In[ ]:




