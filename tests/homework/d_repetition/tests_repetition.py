import unittest


'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers


class Test_Config(unittest.TestCase):

    def test_get_factorial_1(self):
        #test that the function get_factorial with parameter 4 returns the value 24
        self.assertEqual(24, get_factorial(4))

    def test_get_factorial_2(self):
        #test that the function get_factorial with parameter 5 returns the value 120
        self.assertEqual(120, get_factorial(5))   

    def test_get_factorial_3(self):
        #test that the function get_factorial with parameter 6 returns the value 720
        self.assertEqual(720, get_factorial(6)) 

    def test_sum_odd_numbers_1(self):
        #test that the the function sum_odd-numbers with paramter 7 returns 16
        self.assertEqual(16, sum_odd_numbers(7))

    def test_sum_odd_numbers_2(self):
        #test that the the function sum_odd-numbers with paramter 9 returns 25
        self.assertEqual(25, sum_odd_numbers(9))    

    def test_sum_odd_numbers_3(self):
        #test that the the function sum_odd-numbers with paramter 10 returns 25
        self.assertEqual(25, sum_odd_numbers(10))      

