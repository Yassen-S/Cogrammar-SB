# Defining variables to use as containers
words = []
full_name = []
birthday = []

# Using with fuction to open file with correct parameters
with open("DOB.txt", "r+", encoding= "utf-8") as file:
    # Iterating to sperate contents of the file.
    for line in file:
        # Collecting word elements
        words = line.split()
        # Slicing to collect Full Name elements
        full_name.append(words[0:2])        
        # Slicing to collect Birthday elements
        birthday.append(words[2:])

# Creating space and displaying title
print(2 * "\n")
print("Name")

# Seperating elements from list, formatting and displaying
for name in full_name:
    # Formatting utilising join and displaying
    names = ' '.join(name)
    print(names)

# Creating space and displaying title
print(3 * "\n")
print("Birthdate")

# Seperating elements from list, formatting and displaying
for birthdays in birthday:
    # Formatting utilising join and displaying
    birthdate = ' '.join(birthdays)
    print(birthdate)
