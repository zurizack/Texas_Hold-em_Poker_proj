from table import *
from player import *
from deck import *
from dealerbuttom import *
from card import *
import random

if __name__ == '__main__':

    the_table = Table()
    cards = [Card('Hearts', '6'), Card('Hearts', '5'), Card('Hearts', '3'),
         Card('Hearts', '2'), Card('Hearts', 'A'), Card('Hearts', '4'),
         Card('Hearts', '9')]
    
    flash = the_table.find_sequence(cards)
    if len(flash) == 0:
        for card in flash:
            print(card)
    else:
        for card in flash:
            print(card)

