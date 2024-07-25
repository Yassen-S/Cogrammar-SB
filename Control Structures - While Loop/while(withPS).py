# Delcaring the user_entry variable and assigning the int datatype to it
user_entry = int
# Delcaring the entry_count variable and assigning the int datatype to it
entry_count = 0
# Delcaring the entry_count_list variable and assigning the list datatype to it
entry_count_list = []


# Initiating the while loop with a condition.
while user_entry != -1:
    # Initiating validation
    try:
       # Prompting for input.
       user_entry = int(input("Please enter a random number: "))
       # Counting the number of entries
       entry_count += 1
       # Making sure the -1 is not calculated
       if user_entry == -1:
            entry_count = entry_count - 1
       else:
           entry_count_list.append(user_entry)
    # Case for invalid type of entry.
    except ValueError:
       print("Please enter a valid entry")
       continue

# Calculating the average entry number
avg_entry_num = sum(entry_count_list) / entry_count

# Print statement with output
print(f"Average entry number = {avg_entry_num}")
