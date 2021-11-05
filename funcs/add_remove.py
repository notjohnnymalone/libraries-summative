################################
# Summative - Libraries - Add and Remove
# Reid A. Martin
# //funcs/
################################



shopping_list = {}

def add_item(): #Adds item to list
    add = input("What would you like to add?\n>")
    if add not in shopping_list:
        price_add = int(input("What is the price?\n>"))
        shopping_list[add] = price_add
    elif add in shopping_list:
        print("That is already in your list!")
        
        
def remove_item(): #removes item that you type in, and the price that you also type in 
    print_list() #If the item or price don't exist you get booted to menu
    remove = input("What would you like to remove?\n>")
    if remove in shopping_list:
        shopping_list.pop(remove)
    else:
        print("Ya... That's not in there...")
        
        
def clear_list(): #clears the lists
    shopping_list.clear()
    print("List Cleared!")
    
def print_list(): #prints the list in a nice format
    print("\n\nHere is your list!\n-------------")
    for i in shopping_list:
        print("You need to buy", i, ", and that costs $", shopping_list[i]) #for the length of the list, it will print the item and the price
    
def total_cost(): #prints out the toatl cost
    total = 0
    total = sum(shopping_list.values())
    print(f"\nThe total cost is ${total}")
