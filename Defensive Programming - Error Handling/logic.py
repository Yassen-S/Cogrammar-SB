exit = False
count = 0


def working():
    exit = False
    while exit == False:    
        view_summary = input("Would you like it to work now? \nPlease enter Y for Yes or N for No:").upper()
        if view_summary == "Y":
            print("It's working now!!!")
        elif view_summary == "N":
            print("It's working now!!!")
            print("Thank you & Goodbye!!!")
            exit = True
            count = 10
        else:
            if view_summary != "Y" or "N":
                print("Please enter a valid entry!")
                continue


while exit == False:
    if count < 4:
        view_summary = input("There is a logical error in this prgramme! Can you fix it? \nPlease enter Y for Yes or N for No:").upper()
        if view_summary != "Y" or "N":
            print("Please enter a valid entry!")
            count += 1
            continue
        elif view_summary == "Y":
            print("It's working now!!!")
        else:
            print("It's working now!!!")
            print("Thank you & Goodbye!!!")
            exit = True
    else:
        print(" WHAT HAVE YOU DONE!!! ")
        print("* / >,<` *" * 200)
        print(" Only playing with you, actually i think you fixed it! \nTry again")
        exit = True
        working()