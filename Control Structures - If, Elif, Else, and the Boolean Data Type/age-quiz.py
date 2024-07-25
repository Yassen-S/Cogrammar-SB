"""
AIM
The aim of this script is to take user input (age) and filter it into a category.
A statement will be printed according to the category of input (age).

METHODOLOGY
I will prompt the user to enter their age, the input will be converted to integer.
Using an IF statement I will filter/categorise the input (age), 
then I will print a statement for each case. 
The script will keep running in a loop until the user enters an age over 100.

"""
# Decalring a global vaiable to use in a loop, assinging the variable to 0.
user_age = 0

# Opening a loop with a case to keep the script promting for input until input is over 100
while user_age < 101:
    # Using the same variable, prompting the user to input age, reassiging age to variable.
    user_age = int(input("Please enter your age: "))

    # IF, ELIF, ELSE statement to outline conditions of filtering/categorising input.
    # For each case a statement is printed. 
    if user_age > 100:
        print("Sorry you're dead.")
    elif user_age >= 65:
        print("Enjoy your retirement!")
    elif user_age >= 40:
        print("You're over the hill.")
    elif user_age == 21:
        print("Congrats on your 21st!")
    elif user_age < 13:
        print("You qualify for the kiddie discount.")
    else:
        print("Age is but a number.")
