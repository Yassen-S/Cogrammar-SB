# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Line 5 # Syntax error 1 #  Missing brackets from print statement added.
# Line 6    # print "\n" # Syntax error 2 # Uneccessary print statement commented out.

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Line 9 # Syntax error 3 # Incorrect use of "==", replaced with "=". Removed text characters from "age_str". Unwanted indentation removed.
age = int(age_Str) # Line 10 # Syntax error # 4 Unwanted indentation removed.
print(f"I'm {age} years old.") # Syntaxt error 5 # Unwanted indentation removed. # Logical error 1 # Incorrect use of concatination, statement converted to f'string

    # Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # Syntax error # Unwanted indentation removed. # Logical error # Variable declared as str should be float to accomodate the 6 months. (ie 3.5 years)
total_years = age + years_from_now # Syntax error Unwanted indentation removed.

print(f"The total number of years: {total_years}") # Syntax error # Missing brackets from print statement added. Variable in "" within print statement, converted to f'string. # Logical error # Undefined variable "answer_years" replaced with "total_years"

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = int(total_years * 12) # Logical error # Undefined variable "total", replaced with "total_years". Casting to int
print(f"In 3 years and 6 months, I'll be {total_months} months old") # Syntax error # Print statement missing brackets and incorrect format, converted to f'string.

#HINT, 330 months is the correct answer

summary = """

# Summary of errors

# Syntax error 1 #  Missing brackets from print statement added.
# Line 5, Line 17, Line 21

# Syntax error 2 # Uneccessary print statement commented out.
# Line 6

# Syntax error 3 # Incorrect use of "==", replaced with "=". Removed text characters from "age_str". 
# Line 9 

# Syntax error 4 # Unwanted indentation removed.
# Line 9, Line 10, Line 11, Line 14, Line 15

# Syntax error 5 # Variable in "" within print statement, converted to f'string. 
# Line 17 

# Syntax error 6 # Print statement incorrect format, converted to f'string.
# Line 21 

# Logical error 1 # Incorrect use of concatination, statement converted to f'string
# Line 11 

# Logical error 2 # Variable declared as str should be float to accomodate the 6 months. (ie 3.5 years)
# Line 14 

# Logical error 3 # Undefined variable "answer_years" replaced with "total_years"
# Line 17 

# Logical error 4 # Undefined variable "total", replaced with "total_years". Casting to int
# Line 20 

"""

exit = False
while exit == False:    
    view_summary = input("Would you like to see a summary of the errors corrected to make this prgramme work? \nPlease enter Y for Yes or N for No:").upper()
    if view_summary == "Y":
        print(summary)
    elif view_summary == "N":
        print("Thank you & Goodbye!!!")
        exit = True
    else:
        if view_summary != "Y" or "N":
            print("Please enter a valid entry!")
            continue