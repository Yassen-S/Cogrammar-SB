"""
AIM
The aim of this script is to manipulate a string by replacing a character and capitalizing the statement.

METHODOLOGY
I will assign a string to a variable (string) with a unwanted character seperating the words.
I will use the replace method to replace the unwanted character with a space. 
I will also use the upper method to convert all letter to upper case.
Finally I will use 
"""

# Declaring a variable (string) and assigning a statement to it.
string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Printing the statement with the replace method and changing all "!"'s with a blank space.
print(string.replace("!", " "))
# Printing the statement using both replace and upper methods.
print(string.replace("!", " ").upper())
# Reversing the statement
reversed_string = string[::-1]
# Printing the reversed statement with previous formatting
print(reversed_string.replace("!", " ").upper())