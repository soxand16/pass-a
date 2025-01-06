import unittest

from simulation import Card, Deck

class TestCard(unittest.TestCase):

    def setup(self):
        pass

    def testMakeCards(self):
        for value in range(1, 14):
            for suit in ['S', 'D', 'C', 'H']:
                test = Card(value, suit)
                self.assertEqual(test.value, value)
                self.assertEqual(test.suit, suit)


class TestDeck(unittest.TestCase):

    def setup(self):
        pass

    def testMakeDeck(self):
        _ = Deck()

    def testDeckHas52Cards(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def testDeckHasAllUniqueCards(self):
        deck = Deck()
        for value in range(1, 14):
            for suit in ['S', 'D', 'C', 'H']:
                test = Card(value, suit)
                self.assertTrue(test in deck._cards)

    def testDrawCard(self):
        deck = Deck()
        self.assertTrue(isinstance(deck.draw(), Card))

    def testDrawRemovesCardFromDeck(self):
        deck = Deck()
        for i in range(51, 0):
            deck.draw()
            self.assertEqual(len(deck), i)

    def testShuffleDeck(self):
        deck = Deck()
        initial_order = deck._cards.copy()
        deck.shuffle()
        shuffled_order = deck._cards
        self.assertNotEqual(shuffled_order, initial_order)


if __name__ == '__main__':
    unittest.main()
