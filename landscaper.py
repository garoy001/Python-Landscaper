landscaper = {"teeth": True, "money": 0, "items": ["1"], "currently_equipped": "1", "total income": 0 }

shop_items = {  "1": {"name": "Teeth",
                    "price": "none",
                    "income": 1},
                "2":{"name": "Rusty Scissors", 
                   "price": 5,
                   "income": 5}, 
                "3":{"name": "Old-Timey Push Lawnmower", 
                   "price": 25,
                   "income": 50},
                "4":{"name": "Fancy Battery-Powered Lawnmower",
                      "price": 250,
                      "income": 100
                      },
                "5":{"name": "Team of Starving Students",
                      "price": 500,
                      "income": 1000,} } 

available_items = []

dialogue_choices = {"1":"Press 1 to cut lawns", 
                    "2": "Press 2 to enter the shop", 
                    "3": "Press 3 to view stats",
                    "Q": "Press Q to escape\n", 
                    "X":"Press X to exit the shop\n", }
#############################################################################################################
shop_escape = True
space_text = " | "
#############################################################################################################
def check_money():
    if(landscaper["currently_equipped"] == "1" and landscaper["money"] >= 5):
        return True
    elif(landscaper["currently_equipped"] == "2" and landscaper["money"] >= 25):
        return True
    elif(landscaper["currently_equipped"] == "3" and landscaper["money"] >=250):
        return True
    elif(landscaper["currently_equipped"] == "4" and landscaper["money"] >=500):
        return True
    else:
        return False
#############################################################################################################
def check_win_condition():
    if(landscaper["currently_equipped"] == "5" and landscaper["money"] >= 1000):
        print("Congradulations you win!")
        print(r"""\

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   ಠ ಠ. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)
        return True
    else:
        return False
#############################################################################################################
def check_stats():
    print("\n<<-----Stats----->>\n")
    print("Money:                  $"+ str(landscaper["money"]))
    print("Total Money Earned:     $" + str(landscaper["total income"]))
    print("\nItems: ")
    for item in landscaper["items"]:
        print("--"+shop_items[item]["name"])
    print("\nCurrently Equipped: "+shop_items[landscaper["currently_equipped"]]["name"])
    print("")
#############################################################################################################
def shop_options():
    for key,value in shop_items.items():
        if key not in landscaper["items"]:
            available_items.append(value)
#############################################################################################################
def pop_shop():
    available_items.clear()
    counter = 1
    shop_options()
    print("\n<<<<Welcome to the shop!>>>> \n")
    print("Current cash: $" + str(landscaper["money"]) + "\n")
    print("The items available are: ")
    for option in available_items:
        str_counter = str(counter)
        print(f"#{str_counter} - " + option["name"] + " $" + str(option["price"]))
        counter += 1
    print(" ")
#############################################################################################################
def visit_shop():
        while(shop_escape):
            pop_shop()
            item_choice = input(f"Enter the item number to purchase | "+ dialogue_choices["X"]).capitalize()
            if(item_choice == "X"):
                return
            else:
                int_item_choice = int(item_choice) -1
                if(landscaper["money"] >= available_items[int_item_choice]["price"]):
                    landscaper["money"] = landscaper["money"] - available_items[int_item_choice]["price"]
                    for key,value in shop_items.items():
                        if (value["name"] == available_items[int_item_choice]["name"]):
                            landscaper["items"].append(str(key))
                            landscaper["currently_equipped"] = str(key)
                    print(available_items[int_item_choice]["name"] + " equipped!")
                    print()
                    return
                else:
                    print("\nNot enough money!\n")
#############################################################################################################
def check_choice(choice, has_money):
    if(choice == "1"):
        print("\n!!! You have cut the lawn       +$"+str(shop_items[landscaper["currently_equipped"]]["income"]))
        landscaper["money"] += shop_items[landscaper["currently_equipped"]]["income"]
        landscaper["total income"] += shop_items[landscaper["currently_equipped"]]["income"]
        print("Current cash: $" + str(landscaper["money"]) + "\n")
    elif(choice == "2" and has_money == True):
        visit_shop()
    elif(choice == "3"):
        check_stats()

    else:
        print("\nPlease pick one of the options\n")
        return
#############################################################################################################
print("\n######################################################")
print("         Welcome to Lawnmower Text Simulator!\nThe Goal is to purchase the best upgrade and get $1000!\n\n           As you hit financial checkpoints,\n    the shop will appear for purchasing upgrades")
print("######################################################\n")

while(True):
    has_money = False
    if(check_win_condition() == True):
        break
    if(check_money()):
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