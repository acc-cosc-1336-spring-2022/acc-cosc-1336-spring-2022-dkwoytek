import unittest

from src.homework.j_classes.class_a import Die


class Test_Config(unittest.TestCase):
    
    
    def test_die_get_rolled_value(self):
        #test that get_rolled_value returns values 1 to 6 on 3 rolls
        die = Die()
        die.roll()
        roll_1 = die.get_rolled_value()
        self.assertEqual(True, roll_1 >= 1 or roll_1 <= 6)
        die.roll()
        roll_2 = die.get_rolled_value()
        self.assertEqual(True, roll_2 >= 1 or roll_2 <= 6)
        die.roll()
        roll_3 = die.get_rolled_value()
        self.assertEqual(True, roll_3 >= 1 or roll_3 <= 6)
