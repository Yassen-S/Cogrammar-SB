"""
AIM
To convert between float and integer datatypes.

METHODOLOGY
I will declare a set of varibles and convert the datatypes as follows:
num1 to integer
num2 to float
num3 to string
string1 to integer.
I will convert the variables to another datatype using casting."""

# Declaring variables of different datatypes and assigning values.
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# Creating a new variable and casting the value of the original variable. (Converting float to integer)
converted_num1 = int(num1)
# Printing result and confirming datatypes 
print(f"You have converted {num1} with a datatype of: {type(num1)} to {converted_num1} with a datatype of: {type(converted_num1)}")

# Creating a new variable and casting the value of the original variable. (Converting integer to float)
converted_num2 = float(num2)
# Printing result and confirming datatypes
print(f"You have converted {num2} with a datatype of: {type(num2)} to {converted_num2} with a datatype of: {type(converted_num2)}")


# Creating a new variable and casting the value of the original variable. (Converting integer to string)
converted_num3 = str(num3)
# Printing result and confirming datatypes
print(f"You have converted {num3} with a datatype of: {type(num3)} to {converted_num3} with a datatype of: {type(converted_num3)}")


# Creating a new variable and casting the value of the original variable. (Converting string to integer)
converted_string1 = int(string1)
# Printing result and confirming datatypes
print(f"You have converted {string1} with a datatype of: {type(string1)} to {converted_string1} with a datatype of: {type(converted_string1)}")