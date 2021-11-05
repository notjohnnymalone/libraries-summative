#############################
#-- FP3-F01 Modules & Libraries - Main
#-- Reid A. Martin
#############################

from funcs import add_remove, bye


if __name__ == '__main__':
    print("Welcome to the Shopping List")
    while 1:
        menu = input("""What would you like to do?

1. Add to list
2. Remove item from list
3. Clear list
4. Print shopping list
5. Leave
>""")
        if menu == '1':
            add_remove.add_item() #adds item and price
        elif menu == '2':
            add_remove.remove_item() #removes the item and price
        elif menu == '3':
            add_remove.clear_list() #clears shop list
        elif menu == '4':
            add_remove.print_list() #gives list
            add_remove.total_cost() #prints total cost
        elif menu == '5':
            add_remove.print_list() #gives list
            add_remove.total_cost() #prints total cost
            bye.leave_prog() #says goodbye like a polite gentleman
            break
        else:
            print("Huh?") #so you can't break the menu