list = []
game = True
def ask():
    global game
    a = input("What would you like to do?\n-Add an item (a)\n-change an item (c)\n-delete an item (d)\n-view all items (v)\n-quit (q)\n")
    if a == "a":
        item = input("Name the item you want to add:  ")
        list.append(item)
    elif a == "c":
        item = input("Which item would you like to modify?  ")
        newItem = input("Rename this item:  ")
        if item in list:
            index = list.index(item)
            list[index] = newItem
        else:
            print("This item is not in the list!")
    elif a == "d":
        item = input("Which item would you like to remove?  ")
        list.pop(item)
    elif a == "v":
        print(list)
    elif a == "q":
        game = False
    else:
        print("Please type a valid option")
while game:
    ask()