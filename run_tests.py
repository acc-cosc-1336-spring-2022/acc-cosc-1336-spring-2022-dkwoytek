import unittest
'''
the file in /tests/homework/e_functions/tests_functions
has the test functions
'''
from tests.homework.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)


