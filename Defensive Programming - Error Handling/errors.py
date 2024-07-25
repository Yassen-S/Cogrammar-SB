print("Welcome to the error program") 
age_Str = "24"
age = int(age_Str)
print(f"I'm {age} years old.") 


years_from_now = 3.5 
total_years = age + years_from_now
print(f"The total number of years: {total_years}")


total_months = int(total_years * 12)
print(f"In 3 years and 6 months, I'll be {total_months} months old")
print("""
      
      The programme is working!!!
      
      """)

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