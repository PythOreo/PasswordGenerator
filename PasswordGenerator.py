from time import sleep
from random import sample

# Defaulting the lower letters
print("Hello, The lower letters are included by default.")
sleep(1)
# The pwd is by Default contains the lower letters
pwd = "abcdefghijklmnopqrstuvwxyz"
pword = []
# The big variable contains the upper letters
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# The special variable contains the special character
special = "!@#$%^&*:<~"
# The nums variable contains the the numbers 0 : 9
nums = "0123456789"

# defining a function "do_multi_things" to help us do multiple things and decrease lines of code
def do_multi_things(func, var):
    if func == "Y":
        global pwd
        pwd += var
    elif func == "N":
        pass
    else:
        print("Invlaid answer, we will assume that you typed 'N'.")
    print("Wait please....")
    sleep(1)

# Creating a while loop to make sure that the user inputs a number in the length variable
while True:
    try:
        # The length input contains the length of the password
        length = int(input("Please input your password length [less than 25]: "))
        # Cheking the length of the password
        if length > 25:
            print("Too many, please type a smaller than 25")
        else:
            break
    except ValueError:
        print("Invalid, please write a num.")

# adding a neat funcion to make the app looks nicer
print("Wait please.....")
sleep(1)

# Cheking if the user wants the upper letters?
has_big = input("Do you want upper letters in your pwd? (Y/N): ").upper().strip()
do_multi_things(has_big, big)

# Cheking if the user wants numbers?
has_nums = input("Do you want numbers in your pwd? (Y/N): ").upper().strip()
do_multi_things(has_nums, nums)

# Cheking if the user wants the special characters?
has_special = input("Do you want special characters in your pwd? (Y/N): ").upper().strip()
do_multi_things(has_special, special)

# adding the sleep function again
print("Collecting the password.....")
sleep(2)
print("Generating your password.....")
sleep(1.5)

# Using the sample func to create the pword in the length that the user input
pword = sample(pwd, length)
# Making the password variable to convert the pword(which is a list) to a string using the builtin join function
password = "".join(pword)
# Printing the password
print("The generated password is", password)
sleep(1)

                                            #######################################
                                            ## The end of the program, Have fun:)##
                                            #######################################
