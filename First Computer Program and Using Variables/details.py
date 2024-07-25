"""
AIM
The aim of this programme is to collect information from the user and then print a summary of the information collected.

METHODOLOGY
I will be using the "input" function to promt the user to enter information.
Each entry will be stored in a vaiable for later use. The information will be summarised in a single text using f statement.
"""
# Prompting user for input and assigning to a variable. (name)
name = input("Please enter your Name: ")
# Prompting user for input and assigning to a variable. (age)
age = input("Please enter your Age: ")
# Prompting user for input and assigning to a variable. (house_number)
house_number = input("Please enter your House number: ")
# Prompting user for input and assigning to a variable. (street_name)
street_name = input("Please enter your Street name: ")

# Printing an f statement to summarise the input given.
print(f"Your name is {name}, you are {age} years old and you live at {house_number} {street_name}.")