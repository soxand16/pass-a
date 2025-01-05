import unittest

from simulation import Card

class TestCard(unittest.TestCase):

    def setup(self):
        pass

    def testMakeCards(self):
        for value in range(1, 14):
            for suit in ['S', 'D', 'C', 'H']:
                test = Card(value, suit)
                self.assertEqual(test.value, value)
                self.assertEqual(test.suit, suit)

if __name__ == '__main__':
    unittest.main()
