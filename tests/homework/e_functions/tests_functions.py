import unittest


'''
The file at /src/homework/e_in_proc_out/output has 
the function get_hour.
'''
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds
from src.homework.e_functions.value_return import time_from_utc


class Test_Config(unittest.TestCase):

    def test_get_hour(self):
        #test that the function get_factorial with parameter value 3800 returns the value 1
        self.assertEqual(1, get_hour(3800))

    def test_get_hour(self):
        #test that the function get_factorial with parameter value 3600 returns the value 1
        self.assertEqual(1, get_hour(3600))

    def test_get_minutes(self):
        #test that the function get_factorial with parameter value 3800 returns the value 3
        self.assertEqual(3, get_minutes(3800))

    def test_get_minutes(self):
        #test that the function get_factorial with parameter value 3600 returns the value 0
        self.assertEqual(0, get_minutes(3600))

    def test_get_seconds(self):
        #test that the function get_factorial with parameter value 3800 returns the value 20
        self.assertEqual(20, get_seconds(3800))

    def test_get_seconds(self):
        #test that the function get_factorial with parameter value 3600 returns the value 0
        self.assertEqual(0, get_seconds(3600))

    def test_utc_time_to_eastern_standard_time(self):
        self.assertEqual(15, time_from_utc(-5, 20))
    
    def test_utc_time_to_central_standard_time(self):
        self.assertEqual(14, time_from_utc(-6, 20))

    def test_utc_time_to_mountain_standard_time(self):
        self.assertEqual(13, time_from_utc(-7, 20)) 

    def test_utc_time_to_pacific_standard_time(self):
        self.assertEqual(12, time_from_utc(-8, 20))  
          