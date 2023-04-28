import re

validation_condition = "^[a-z]+[\._]?+[a-z 0-9]+[@]\w+[.]\w{3,4}$"
gmail = input("please Enter your email : ")

if re.search(validation_condition, gmail):
    print("Your gmail is valid gamil")
else:
    print("Please enter valid gmail")    