import files

inventory = {}
menu_selex = "y"

while menu_selex == "y":   #This is so that HW 7 Menu is generated
    print('\nHomework 7 Menu\n1-Add or Update Item\n2-Display Items\n3-Exit')
    selex = int(input('Please select menu item 1, 2 or 3: ')) 

    if selex == 1:   #This is the Add or Update Item part of the assignment
        print('Please add or update your inventory item.')
        widget_name = input('Enter name of item: ')
        try:
          widget_quantity = int(input('Enter quantity of item added to inventory (as a positive number) or sold from inventory (as negative number): '))
          files.add_inventory(inventory, widget_name, widget_quantity)
        except ValueError:
             print('Data entry error. Quantity entered must be entered as a numeric integer data amount.')
        
    elif selex == 2:   #This is the Display Items part of the assignment
         files.write_to_file(inventory)
         files.read_from_file()

    elif selex == 3:   #This is the exit from the menu part of the assignment
         print('You have chosen to exit.')
    
    else:
         print("Invalid entry")

    menu_selex = input('Do you want to continue with another menu selection (Enter "y" for yes, n to exit from Homework 7 Menu): ')

