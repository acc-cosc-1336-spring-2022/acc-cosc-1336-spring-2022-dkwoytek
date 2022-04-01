import unittest


from src.homework.h_strings.strings import get_hamming_distance 
from src.homework.h_strings.strings import get_dna_complement
class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        #test that the function returns 7
        dna1 = ['G', 'A', 'G', 'C', 'C', 'T', 'A', 'C', 'T', 'A', 'A', 'C', 'G', 'G', 'G', 'A', 'T']
        dna2 = ['C', 'A', 'T', 'C', 'G', 'T', 'A', 'A', 'T', 'G', 'A', 'C', 'G', 'G', 'C', 'C', 'T']
        self.assertEqual(7, get_hamming_distance(dna1, dna2))

    def test_get_dna_complement(self):
        dna = ['A', 'A', 'A', 'A', 'C', 'C', 'C', 'G', 'G', 'T']
        complement = ['A', 'C', 'C', 'G', 'G', 'G', 'T', 'T', 'T', 'T']
        self.assertEqual(complement, get_dna_complement(dna))
        
