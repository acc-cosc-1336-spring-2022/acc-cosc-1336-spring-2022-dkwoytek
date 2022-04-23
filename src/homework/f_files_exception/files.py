def add_inventory(inventory, widget_name, widget_quantity):
    if widget_name not in inventory:            #add the widget to the inventory
        inventory[widget_name] = widget_quantity
    else:                                       #update the inventory of widgets 
        inventory[widget_name] += widget_quantity
    
def remove_inventory_widget(inventory, widget_name):
    if widget_name in inventory:
        del inventory[widget_name]
        print('Record deleted')
    else:
        print('Item not found.')

def write_to_file(inventory):
    inventory_file = open('inventory.txt', 'w')
    for key, value in inventory.items():
        inventory_file.write(key + '\n')
        inventory_file.write(str(value) + '\n')
    inventory_file.close()

def read_from_file():
    try:
        inventory_file = open('inventory.txt', 'r') 
        inventory_item = inventory_file.readline()
        while inventory_item != '': # reads from file and displays items
            inventory_quantity = inventory_file.readline()
            print('Inventory item:', inventory_item.rstrip('\n'), end='  ')
            print('Inventory quantity:', inventory_quantity.rstrip('\n'))
            inventory_item = inventory_file.readline()
        inventory_file.close
    except IOError:
        print('This inventory file does not exist.')
