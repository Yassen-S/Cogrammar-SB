"""
AIM
The aim of this script of to produce a pattern out of the "*" character.
The size of the pattern will depend on a range, and I am required to
make use of the FOR loop and IF, ELSE statement.

METHODOLOGY
I will use a container to store each line of the pattern as it being generated. 
Once the pattern has reached its peak number of characters, I will remove the last 
character and reverse the pattern. This process will effectivley produce the 
desired pattern.

"""

print("Example pattern: ")
# Creating a variable and assigning an empty list to it.
res = []
# Initiating FOR loop to iterate over a range of numbers.
for i in range(1, 7):
    # Using an IF statement to seperate the two sections of the pattern.
    if i < 6:
        # For each iteration a number of stars will be added to the list.
        res.append(i * "*")
        # Also each line will be printed along the way.
        print(i * "*")
    # Once the first condition becomes false
    else:
        # The last element will be removed from the list.
        res.pop(-1)
        # The list is being reversed.
        res.reverse()
        # Printing the reversed list in correct format.
        print(*res, sep='\n')


# Let us consider a condition where we would like to specify the range and,
# ultimately choose the size of the pattern. I will try to improve the code.


print("Now you choose the size!")

# Creating a variable and assigning an empty list to it.
res = []

# Using a Boolean and WHILE loop to validate input   
pattern = False
while pattern == False:
    try:
        # Assiging an input to a variable to use in the range of FOR loop.
        limit = int(input("Please enter a number to specify the widest point in the pattern: ")) + 2
        # Case for exiting the loop
        pattern = True
    except ValueError:
        # Case for TypeError
        print("Please enter a valid entry")
        continue
# Initiating FOR loop to iterate over a range from 1 to limit(input number by user).
for i in range(1, limit):
    # Using an IF statement to seperate the two sections of the pattern.
    if i < (limit - 1):
        # For each iteration a number of stars will be added to the list.
        res.append(i * "*")
        # Also each line will be printed along the way.
        print(i * "*")
    # Once the first condition becomes false
    else:
        # The last element will be removed from the list.
        res.pop(-1)
        # The list is being reversed.
        res.reverse()
        # Printing the reversed list in correct format.
        print(*res, sep='\n')