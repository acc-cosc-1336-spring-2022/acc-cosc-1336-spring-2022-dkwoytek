import unittest


#from src.homework.i_dictionaries_sets.dictionary import get_p_distance
#from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix
from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget

class Test_Config(unittest.TestCase):

    # def test_p_distance(self):
    #     #test that the function returns 0.4
    #     list1 = ['T','T','T','C','C','A','T','T','T','A']
    #     list2 = ['G','A','T','T','C','A','T','T','T','C']
    #     self.assertEqual(0.4, get_p_distance(list1,list2))

    # def test_get_p_distance_matrix(self):
    #     #test the get_p_distance_matrix with parameter value
    #     dataset = [ ['T','T','T','C','C','A','T','T','T','A'],
    #                 ['G','A','T','T','C','A','T','T','T','C'],
    #                 ['T','T','T','C','C','A','T','T','T','T'],
    #                 ['G','T','T','C','C','A','T','T','T','A']   ]

    #     p_distance_matrix = [    [0.0, 0.4, 0.1, 0.1],
    #                              [0.4, 0.0, 0.4, 0.3],
    #                              [0.1, 0.4, 0.0, 0.2],
    #                              [0.1, 0.3, 0.2, 0.0]   ]
    #     self.assertEqual(p_distance_matrix, get_p_distance_matrix(dataset))

    def test_add_inventory(self):
        #test that the function returns correct inventory amount
        inventory = {}
        widget_name = 'Widget1'
        widget_quantity = 10
        add_inventory(inventory, widget_name, widget_quantity)
        self.assertEqual(inventory[widget_name], 10)

        widget_quantity = 25
        add_inventory(inventory, widget_name, widget_quantity)
        self.assertEqual(inventory[widget_name], 35)

        widget_quantity = -10
        add_inventory(inventory, widget_name, widget_quantity)
        self.assertEqual(inventory[widget_name], 25)

    def test_remove_inventory_widget(self):
        #test length of dictionary equals 1 and that widget2 still exists
        inventory = {}
        inventory['widget1'] = 5
        inventory['widget2'] = 10
        remove_inventory_widget(inventory, 'widget1')
        self.assertEqual(1, len(inventory)) 
        self.assertEqual(inventory['widget2'], 10)


