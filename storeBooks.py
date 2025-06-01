inventory = {}
count = True
while count == True:
    answer = input("What would you like to do?\n-Add/change a book (a)\n-Show all books (s)\n-Delete a book (d)\n-Quit (q)\n")
    if answer == "a":
        book = input("Enter the book name: ")
        cost = input("Enter the cost: $")
        inventory[book] = cost
    elif answer == "s":
        ans = input("What information do you want? (titles/costs/both)")
        if ans == "titles":
            print(inventory.keys())
        elif ans == "costs":
            print(inventory.values())
        elif ans == "both":
            print(inventory)
    elif answer == "d":
        book = input("Which book would you like to remove? ")
        del(inventory[book])
    elif answer == "q":
        count = False
