# table.py
from player import Player
from deck import Deck
from card import *

class Table:
    def __init__(self):
        self.places = {i: None for i in range(1, 10)}
        self.community_cards = []
        self.pot = 0
        self.last_bet_size = 0
        self.last_player = None


    def add_player(self, player_object, chair_number=None):
        if not isinstance(player_object, Player):
            print("Invalid player object. Please provide an instance of the Player class.")
            return False

        if chair_number is not None:
            if 1 <= chair_number <= 9:
                if self.places[chair_number] is None:
                    self.places[chair_number] = player_object
                    return True
                else:
                    print(f"Chair {chair_number} is already occupied.")
            else:
                print("Invalid chair number. Please choose a chair between 1 and 9.")
        else:
            for chair_number, player in self.places.items():
                if player is None:
                    self.places[chair_number] = player_object
                    return True
            print("No free chair available.")
        return False

    def remove_player(self, player_object):
        for chair_number, player in self.places.items():
            if player == player_object:
                self.places[chair_number] = None
                return True
        print("Player not found at the table.")
        return False

    def upd_pot(self,amount):
        self.pot += amount

    def reset_pot(self):
        self.pot = 0

    def get_pot(self):
        return self.pot
    
    def add_community_card(self, card):
        self.community_cards.append(card)

    def get_community_cards(self):
        return self.community_cards
    
    def reset_community_cards(self):
        self.community_cards = []

    def get_last_bet_size(self):
        return self.last_bet_size
    
    def upd_last_bet_size(self,amount):
            self.last_bet_size = amount

    def reset_last_bet_size(self):
        self.last_bet_size = 0
    
    def get_playersit_by_name(self,name):
        for seat_number, player in self.places.items():
            if player.get_name() == name:
                return seat_number
            return None

    def upd_last_player(self,last_player):
        self.last_player = last_player

    def reset_last_player(self):
        self.last_player = None

    def get_last_player(self):
        return self.last_player
    
    def find_flash(self,cards):
        suits = {'Clubs': 0, 'Diamonds': 0, 'Hearts': 0, 'Spades': 0}
        
        for card in cards:
            suit = card.get_card()[0]  # Get the last character of the card to determine the suit
            suits[suit] += 1
        
        max_count = max(suits.values())
        max_suit = max(suits, key=suits.get)
        
        if max_count < 5:
            return False
        else:
            same_suit_cards = [card for card in cards if card.get_card()[0] == max_suit]
            return same_suit_cards
    

    def find_sequence(self,cards):


        sorted_cards = sorted(cards, key=lambda card: card.get_card()[1])
        longSequence = 1
        longSequencelist = []
        currentSequence = 1
        currentSequencelist = []
        for i in range(len(sorted_cards)-1):
            if self.get_card_value(sorted_cards[i+1]) != self.get_card_value(sorted_cards[i]):
                currentSequencelist.append(sorted_cards[i])
                
                if self.get_card_value(sorted_cards[i+1]) == self.get_card_value(sorted_cards[i])+1:
                    currentSequence +=1
                else:
                    if currentSequence > longSequence:
                        longSequencelist.clear()
                        for i in range(len(currentSequencelist)):
                            longSequencelist.append(currentSequencelist[i])
                    longSequence = max(longSequence, currentSequence)
                    currentSequencelist.clear()
                    currentSequence = 1

        if len(longSequencelist) >= 5:
            return longSequencelist
        else:
            return []
        


            

        
    def get_card_value(self,card):
        royal_values = {'2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,'J': 11, 'Q': 12, 'K': 13, 'A': 1, 'A': 14}
        return royal_values[card.get_card()[1]]


        
