


import math


def investment():
    deposit_amount = int(input("Please enter the amount of money you are depositing: "))
    interest_rate = int(input("Please enter the interest rate as a whole number: ")) / 100
    investment_years = int(input("Please enter the number of years you would like to invest for: "))
    interest_type_val = False
    while interest_type_val == False:
        
        interest_type = input("Please enter the type of interest you would like, simple or compound: ").lower()

        simple_interest  = deposit_amount * (1 + interest_rate * investment_years)

        compound_interest = deposit_amount * math.pow((1 + interest_rate), investment_years)

        if interest_type == "simple":
            interest_type_val = True
            print(f"Your total return using 'simple interest' will be £{simple_interest}, over a period of {investment_years} years.")
        elif interest_type == "compound":
            interest_type_val = True
            print(f"Your total return using 'compound interest' will be £{compound_interest}, over a period of {investment_years} years.")
        else:
            interest_type_val = False
            print(f"'{interest_type}' is not a valid entry, please enter a valid selection:")
        
        

def bond():
    house_value = int(input("Please enter the current value of the house: "))
    interest = round(float(input("Please enter the interest rate: ")) / 100, 2)
    months = int(input("Please enter the number of months you would like to repay the bond: "))
    monthly_interest = interest / 12

    repayment = round(float((monthly_interest * house_value) / (1 - (1 + monthly_interest)**(-months))), 2)

    print(f"""
          
                Your house value is £{house_value}, the interest rate you have entered is {interest*100}%. 
                You have chosen to pay back over {months} months and your monthly paymnents will be equal to £{repayment}.
                Over {months} months you will pay £{round(repayment * months, 2)}.

    """)

def first_screen():
    programme_type_val = False

    while programme_type_val == False:
        programme_type = input("""
            investment - to calculate the amount of interest you'll earn on your investment
            bond       - to calculate the amount you'll have to pay on a home loan
        
            Enter either 'investment' or 'bond' from the menu above to proceed:
            """).lower()

        if programme_type == "investment":
            programme_type_val = True
            investment()
        elif programme_type == "bond":
            programme_type_val = True
            bond()
        else:
            programme_type_val = False
            print(f"'{programme_type}' is not a valid entry, please type either 'investment' or 'bond': ")
first_screen()