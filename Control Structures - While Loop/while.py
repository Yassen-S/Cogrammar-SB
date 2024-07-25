user_entry = int
entry_count = 0
entry_count_list = []

while user_entry != -1:
    try:
       user_entry = int(input("Please enter a random number: "))
       entry_count += 1
       if user_entry == -1:
            entry_count = entry_count - 1
       else:
           entry_count_list.append(user_entry)
    except ValueError:
       print("Please enter a valid entry")
       continue

avg_entry_num = sum(entry_count_list) / entry_count

print(f"Average entry number = {avg_entry_num}")