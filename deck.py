# deck.py
from card import Card
import random

class Deck:
    def __init__(self):
        self.suits = ["h", "c", "s", "d"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.stack = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.stack)

    def deal_card(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None