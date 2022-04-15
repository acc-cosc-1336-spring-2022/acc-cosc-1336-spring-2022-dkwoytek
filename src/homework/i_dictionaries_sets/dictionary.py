

# def get_p_distance(list1, list2):
#     index = 0
#     difference = 0
#     while index < len(list1):
#         if list1[index] != list2[index]:
#             difference +=1
#         index +=1
#     p_distance = difference / len(list1)
#     return p_distance

# def get_p_distance_matrix(dataset):
#     p_distance_matrix = []
#     for row_list in dataset:
#         row = []
#         for column_list in dataset:
#             row.append(get_p_distance(row_list,column_list))
#         p_distance_matrix.append(row)
#     return p_distance_matrix

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



