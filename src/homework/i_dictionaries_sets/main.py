import dictionary


# menu_selex = "y"
# while menu_selex == "y":   #This is so that HW Menu is generated
#     print('\nHomework 6 Menu\n1-Get p distance matrix\n2-Exit')
#     selex = int(input('Please select menu item 1 or 2: ')) 

#     if selex == 1:   #This is the p distance matrix part of the assignment
#         print('Please provide your collection of 10 or less DNA strings of equal length.\nYou must enter only the letters of the DNA bases with no spaces between letters!')
#         dataset = []
#         again = "y"
#         while again == "y":
#             DNA_string = input('Enter a DNA string using this format XXXXXX: ')
#             DNA_list = list(DNA_string)
#             dataset.append(DNA_list)
#             print('Do you want to add another DNA string?')
#             again = input('Enter "y" for yes, n for no: ')
#         print('Here are the DNA strings you entered: ')
#         for string in dataset:
#             print(string)
#         print('This is the p distance matrix for those DNA strings is:')
#         p_distance_matrix = dictionary.get_p_distance_matrix(dataset)
#         for row in p_distance_matrix:
#             for item in row:
#                 print(format(item,'8.3f'), end=' ')
#             print('')

#     elif selex == 2:   #This is the exit from the menu part of the assignment
#          print('You have chosen to exit.')
    
#     else:
#          print("Invalid entry")

#     menu_selex = input('Do you want to continue with another menu selection (Enter "y" for yes, n to exit from Homework 6 Menu): ')

inventory = {}
menu_selex = "y"

while menu_selex == "y":   #This is so that HW 7 Menu is generated
    print('\nHomework 7 Menu\n1-Add or Update Item\n2-Delete Item\n3-Exit')
    selex = int(input('Please select menu item 1, 2 or 3: ')) 

    if selex == 1:   #This is the Add or Update Item part of the assignment
        print('Please add or update your inventory item.')
        widget_name = input('Enter name of item: ')
        widget_quantity = int(input('Enter quantity of item added to inventory (as a positive number) or sold from inventory (as negative number): '))
        dictionary.add_inventory(inventory, widget_name, widget_quantity)
        
    elif selex == 2:   #This is the Delete Item part of the assignment
        widget_name = input('Enter name of item to be removed fom inventory: ')
        dictionary.remove_inventory_widget(inventory, widget_name)         

    elif selex == 3:   #This is the exit from the menu part of the assignment
         print('You have chosen to exit.')
    
    else:
         print("Invalid entry")

    menu_selex = input('Do you want to continue with another menu selection (Enter "y" for yes, n to exit from Homework 7 Menu): ')






