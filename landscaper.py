landscaper = {"teeth": True, "money": 0, "items": []}

shop_items = {"1":{"name": "scissors", 
                   "price": 5}, 
              "2":{"name": "lawnmower", 
                   "price": 25}}

available_items = []

dialogue_choices = {"1":"Press 1 to cut lawns", 
                    "2": "Press 2 to enter the shop", 
                    "3": "Press 3 to view stats",
                    "Q": "Press Q to escape\n", 
                    "X":"Press X to exit the shop\n", }


shop_escape = True
space_text = " | "

def check_stats():
    print("\n<<-----Stats----->>")
    print("Money:  $"+ str(landscaper["money"]))
    print("Items: ")
    for item in landscaper["items"]:
        print("--"+item["name"])
    print("")

def shop_options():
    for key,value in shop_items.items():
        if key not in landscaper["items"]:
            available_items.append(value)

def pop_shop():
    available_items.clear()
    counter = 1
    shop_options()
    print("The items available are: ")
    for option in available_items:
        str_counter = str(counter)
        print(f"#{str_counter} - " + option["name"] + " " + str(option["price"]))
        counter += 1
    print(" ")

def visit_shop():
        while(shop_escape):
            pop_shop()
            item_choice = input(f"Enter the item number to purchase | "+ dialogue_choices["X"]).capitalize()
            if(item_choice == "X"):
                return
            else:
                int_item_choice = int(item_choice) -1
                if(int_item_choice > available_items[int_item_choice]["price"]):
                    landscaper["items"].append(available_items[int_item_choice])
                    print(available_items[int_item_choice]["name"] + " added to inventory!")
                    print()
                else:
                    print("\nNot enough money!\n")

def check_choice(choice, has_money):
    if(choice == "1"):
        print("\n!!! You have cut the lawn       +$1\n")
        landscaper["money"] += 1
    elif(choice == "2" and has_money == True):
        visit_shop()
    elif(choice == "3"):
        check_stats()

    else:
        print("\nPlease pick one of the options\n")
        return


while(True):
    has_money = False
    if(landscaper["money"] >= 5):
        has_money = True
        choice = input(dialogue_choices["1"] + space_text + dialogue_choices["2"] + space_text +dialogue_choices["3"]+space_text+ dialogue_choices["Q"] ).capitalize()
        if(choice == "Q"):
            break
        check_choice(choice, has_money)
    else:
        choice = input(dialogue_choices["1"]+ space_text +dialogue_choices["3"]+space_text+ dialogue_choices["Q"]).capitalize()
        if(choice == "Q"):
            print("Thanks for playing!")
            break
        check_choice(choice, has_money)
    

