import random

"""
AIM
The aim of this script detirmine the award a person competing in a triathlon wiil receive.

METHODOLOGY
I will use the random function to generate the different times for indiviual events in the
triathlon for an athlete. Then I will combine these event times to get a total time.
The total time will detirmine the award the athlete will receive. The athletes name along with
invdividual event times, total time and award gained will be printed.


"""
# Assigning a variable globally to use in a loop and calculation.
total_time = 0

# Initiating while loop to keep the script prompting until the athlete receives "No award"
while total_time <112:
    # Prompting user for athlete name, assiging value to a variable.
    athlete_name = input("Please enter the name of the athlete: ")

    # Generating a random event time for the athlete.
    swimming_time = random.randint(22, 45)
    # Printing the athlete name along with specific event time.
    print(f"{athlete_name}'s swimmming time = {swimming_time}")

    # Generating a random event time for the athlete.
    cycling_time = random.randint(22, 45)
    # Printing the athlete name along with specific event time.
    print(f"{athlete_name}'s cycling time = {cycling_time}")

    # Generating a random event time for the athlete.
    running_time = random.randint(22, 45)
    # Printing the athlete name along with specific event time.
    print(f"{athlete_name}'s running time = {running_time}")

    # Calculating the total time in mins.
    total_time = swimming_time + cycling_time + running_time
    # Printing the athletes name along with the total time.
    print(f"{athlete_name}'s Total time for triathlon = {total_time} Mins")

    # IF, ELIF statement to determine the award achieved based on total time.
    if total_time >= 111:
        award = "No award"
    elif total_time >= 106:
        award = "Provincial Scroll"
    elif total_time >= 101:
        award = "Provincial Half Colours"
    elif total_time >= 0 and total_time <= 100:
        award = "Provincial Colours"
    # Printing a statement to display athlete name and award achieved.
    print(f"The award achieved by {athlete_name} is {award}")