import math

"""
AIM
I aim to create a script to calculate two different financial calculations. The user should be
able to choose which calculation they want to perform. Also the should be able to input information 
to make the calculations specific

METHODOLOGY
I intend to do this by creating a function for each calculation and a final function for the menu screen.
Finaly I will call the first screen, giving the option to run either calculation function.

"""
# Declaring a function to wrap the investment calculation in.
def investment():
    # Prompting for relavent user input and assigning to variables.
    deposit_amount = int(input("Please enter the amount of money you are depositing: "))
    interest_rate = int(input("Please enter the interest rate as a whole number: ")) / 100
    investment_years = int(input("Please enter the number of years you would like to invest for: "))
    # Declaring a variable to validate input for interest_type
    interest_type_val = False
    # Initiating a while loop to validate input and calculate interest.
    while interest_type_val == False:
        # Prompting user for input to select type of interest
        interest_type = input("Please enter the type of interest you would like, simple or compound: ").lower()
        # Declaring the formula for simple interest and assigning to variable.
        simple_interest  = deposit_amount * (1 + interest_rate * investment_years)
        # Declaring the formula for compound interest and assigning to variable.
        compound_interest = deposit_amount * math.pow((1 + interest_rate), investment_years)

        # IF, ELIF, ELSE statement to validate input for interest_type and print the relavent summary
        if interest_type == "simple":
            interest_type_val = True
            print(f"Your total return using 'simple interest' will be £{simple_interest}, over a period of {investment_years} years.")
        elif interest_type == "compound":
            interest_type_val = True
            print(f"Your total return using 'compound interest' will be £{compound_interest}, over a period of {investment_years} years.")
        else:
            interest_type_val = False
            print(f"'{interest_type}' is not a valid entry, please enter a valid selection:")       
        
# Declaring a function to wrap the bond calculation in.
def bond():
    # Prompting for relavent user input and assigning to variables.
    house_value = int(input("Please enter the current value of the house: "))
    interest = round(float(input("Please enter the interest rate: ")) / 100, 2)
    months = int(input("Please enter the number of months you would like to repay the bond: "))
    # Declaring monthly_interest variable for later use.
    monthly_interest = interest / 12

    # Declaring the formula for monthly repayment amount and assigning to a variable.
    repayment = round(float((monthly_interest * house_value) / (1 - (1 + monthly_interest)**(-months))), 2)

    # Printing summary statement
    print(f"""
          
                Your house value is £{house_value}, the interest rate you have entered is {interest*100}%. 
                You have chosen to pay back over {months} months and your monthly paymnents will be equal to £{repayment}.
                Over {months} months you will pay £{round(repayment * months, 2)}.

    """)

# Declaring a function to provide otptions for calculation.
def first_screen():
    # Declaring a variable to use for validation
    programme_type_val = False

    # Initiating a while loop to validate input.
    while programme_type_val == False:
        # Prompting user for input to select calculation type.
        programme_type = input("""
            investment - to calculate the amount of interest you'll earn on your investment
            bond       - to calculate the amount you'll have to pay on a home loan
        
            Enter either 'investment' or 'bond' from the menu above to proceed:
            """).lower()
        # IF, ELIF, ELSE statement to validate input and call the relavent function.
        if programme_type == "investment":
            programme_type_val = True
            investment()
        elif programme_type == "bond":
            programme_type_val = True
            bond()
        else:
            programme_type_val = False
            print(f"'{programme_type}' is not a valid entry, please type either 'investment' or 'bond': ")

# Calling function to initiate the script.
first_screen()