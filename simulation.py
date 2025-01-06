import random
from collections import namedtuple

Card = namedtuple('Card', ['value', 'suit'])


class Deck():

    def __init__(self):
        self._cards = [Card(value, suit) for value in range(1, 14)
                       for suit in ['S', 'D', 'C', 'H']
                       ]

    def __len__(self):
        return len(self._cards)

    def draw(self):
        return self._cards.pop(0)

    def shuffle(self):
        random.shuffle(self._cards)
