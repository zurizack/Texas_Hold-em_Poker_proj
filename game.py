from table import *
from player import *
from deck import *
from dealerbuttom import *
from card import *
import random

class Game:
    def __init__(self):
        self.deck = Deck()
        self.table = Table()
        self.dealer_buttom = None
        self.players = []

    def add_player(self, player):
        """
        Add a player to the game.
        """
        self.players.append(player)

    def set_dealer(self):
        """
        Set the dealer randomly from the occupied seats.
        """
        occupied_seats = [seat_number for seat_number, player_name in self.table.places.items() if player_name]
        if occupied_seats:
            dealer_seat = random.choice(occupied_seats)
            self.dealer_buttom = Dealerbuttom(dealer_seat)

    def deal_cards(self):
        for _ in range(2):
            for position, player in self.table.places.items():
                if player:  # Check if a player is sitting at the position
                    card = self.deck.deal_card()
                    player.add_card(card)
                    if not player.get_still_in_hand():
                        player.upd_still_in_hand()

    def start(self):
        """
        Start the game.
        """

        # Shuffle the deck
        self.deck.shuffle()

        # Add players to the table
        for player in self.players:
            self.table.add_player(player)
        
        for seat_number,player in self.table.places.items():
            if player:
                print(seat_number,":",player.get_name()," ",end="")

        print("")
        
        # set the dealer position
        self.set_dealer()
        occupied_seats = [seat_number for seat_number, player in self.table.places.items() if player]
        print("dealer in sit: ",self.dealer_buttom,"player is:",self.table.places[occupied_seats[self.dealer_buttom.get_position()-1]].get_name())


        # Start each hand
        while True:  # You can modify this loop condition to end the game after a certain number of hands or under specific conditions
            self.start_hand()

            break
            # Perform other necessary actions for each hand, such as dealing community cards and betting rounds

    def start_hand(self):

        """
        Start a new hand (preflop, flop, turn, river, showdown).
        """
        # dealing card to player
        self.deal_cards()

        
        # list with the nums of sit where occupied by player
        occupied_seats = [seat_number for seat_number, player in self.table.places.items() if player]
        
        #make the blindes
        big_blind_pos = (self.dealer_buttom.get_position() + 1) % len(occupied_seats)
        small_blind_pos = (self.dealer_buttom.get_position()) % len(occupied_seats)
        big_blind = self.table.places[occupied_seats[big_blind_pos]]
        small_blind = self.table.places[occupied_seats[small_blind_pos]]
        
        small_blind.bet_call_raise(1)
        big_blind.bet_call_raise(2)
        self.table.upd_pot(3)
        self.table.upd_last_bet_size(2)

        print("sb : ",small_blind.get_name(),"  size : ",small_blind.get_curent_in_pot())
        print("bb : ",big_blind.get_name(),"  size : ",big_blind.get_curent_in_pot())
        
        # current_position for dealer to set the start position to be utg
        start_position = (self.dealer_buttom.get_position() + 3) % len(occupied_seats)
        
        # pre flop round
        self.round(occupied_seats,start_position -1)

        # add flop to community card
        for _ in range(3):
            self.table.add_community_card(self.deck.deal_card())

        # print("the flop: ",self.table.get_community_cards())
        for card in self.table.get_community_cards():
            print(card,",", end="")
        print(" ")
        # current_position for dealer to set the start position to be sb
        start_position = (self.dealer_buttom.get_position()) % len(occupied_seats)

        # flop round
        self.round(occupied_seats,start_position)

        # add trn to community card
        self.table.add_community_card(self.deck.deal_card())

        # print("the trn: ",self.table.get_community_cards())
        for card in self.table.get_community_cards():
            print(card,",", end="")
        print(" ")
        # trn round
        self.round(occupied_seats,start_position)

        # add river to community card
        self.table.add_community_card(self.deck.deal_card())

        # print("the flop: ",self.table.get_community_cards())
        for card in self.table.get_community_cards():
            print(card,",", end="")
        print(" ")
        # river round
        self.round(occupied_seats,start_position)

    def pre_flop(self,occupied_seats,current_position):

        while True:
            
            player = self.table.places[occupied_seats[current_position]]

            print("curent bet:   ", self.table.get_last_bet_size())

            for idx in occupied_seats:
                print(idx,":",self.table.places[occupied_seats[idx-1]])
            
            if player.get_still_in_hand():
                print("this player cur int pot:",player.get_curent_in_pot())
                action = player.get_action(self.table.get_last_bet_size())
                
                if action == "all in":
                    self.handle_allin_action(player)

                elif action == "call":
                    self.handle_call_action(player)

                elif action == "raise":
                    self.handle_raise_action(player)

                elif action == "fold":
                    player.fold()
                    # players who have folded
                    print(f"{player.get_name()} has folded.")

                else:
                    player.check()
                    self.end_round(occupied_seats)
                    break
            else:
                # Skip players who have folded
                print(f"{player.get_name()} has folded.")

            # Move to the next player in a circular manner
            current_position = (current_position + 1) % len(occupied_seats)
            next_player = self.table.places[occupied_seats[current_position]]

            # Check if the round is complete
            if next_player.get_curent_in_pot() == self.table.get_last_bet_size():
                self.end_round(occupied_seats)
                break

    def round(self,occupied_seats,start_position):

        current_position = start_position
        # current_position
        # print the player in the occupied seats on the table
        # the index in occupied_seats list start from 0 but the value from 1
        for sit in occupied_seats:
            if self.table.places[occupied_seats[sit-1]].get_still_in_hand():
                print("player:",self.table.places[occupied_seats[sit-1]])

        self.table.upd_last_player(self.table.places[occupied_seats[current_position]])

        while True:

            print("curent pot: ",self.table.get_pot() , " curent bet:   ", self.table.get_last_bet_size())

            # take the player obj in the current seat
            # start from sb
            # becuse the occupied_seats list start from 0 it will be the player after the current_position value
            player = self.table.places[occupied_seats[current_position]]

            if player.get_still_in_hand():
                action = player.get_action(self.table.get_last_bet_size())

                if action == "all in":
                    self.handle_allin_action(player)

                elif action == "call":
                    self.handle_call_action(player)

                elif action == "raise":
                    self.handle_raise_action(player)

                elif action == "fold":
                    player.fold()

                else:
                    player.check()

            else:
                # Skip players who have folded
                print(f"{player.get_name()} has folded.")

            # Move to the next player in a circular manner
            next_position = (current_position + 1) % len(occupied_seats)
            next_player = self.table.places[occupied_seats[next_position]]

            if self.table.get_last_player().get_name() == next_player.get_name():
                self.end_round(occupied_seats)
                break

            current_position = next_position


    def end_round(self,occupied_seats):
        for _ in range(len(occupied_seats)):
            player = self.table.places[occupied_seats[_]]
            player.reset_curent_in_pot()
            self.table.reset_last_player()
            self.table.reset_last_bet_size()

    def end_hand():
        pass

    def handle_call_action(self,player_obj):
        call_amount = self.table.get_last_bet_size() - player_obj.get_curent_in_pot()
        self.table.upd_pot(call_amount)
        player_obj.bet_call_raise(call_amount)

    def handle_raise_action(self,player_obj):
        print("player_obj.curent_in_pot() : ",player_obj.get_curent_in_pot())
        raise_amount = int(input(f"{player_obj.get_name()} , please choose amount to raise from: {max(self.table.get_last_bet_size()*2,2)} to: {player_obj.get_stack()}\n"))
        print("player_obj.curent_in_pot() : ",player_obj.get_curent_in_pot())
        if raise_amount > player_obj.get_stack():
            self.handle_allin_action(player_obj)
        elif raise_amount < max(self.table.get_last_bet_size()*2,2):
            raise_amount = max(self.table.get_last_bet_size()*2,2) -  player_obj.get_curent_in_pot()
            self.table.upd_last_bet_size(raise_amount + player_obj.get_curent_in_pot())
            self.table.upd_pot(raise_amount)
            player_obj.bet_call_raise(raise_amount)
            self.table.upd_last_player(player_obj)
        else:
            raise_amount -= player_obj.get_curent_in_pot()
            print("raise_amount : ",raise_amount)
            self.table.upd_last_bet_size(raise_amount + player_obj.get_curent_in_pot())
            self.table.upd_pot(raise_amount)
            player_obj.bet_call_raise(raise_amount)
            self.table.upd_last_player(player_obj)

    def handle_allin_action(self,player_obj):
        self.table.upd_pot(player_obj.get_stack())
        all_in_amount = player_obj.get_stack() + player_obj.get_curent_in_pot()
        if (all_in_amount) > self.table.get_last_bet_size():
            self.table.upd_last_bet_size(all_in_amount)
            self.table.upd_last_player(player_obj)
        player_obj.bet_call_raise(player_obj.get_stack())

if __name__ == '__main__':

        # occupied_seats = [seat_number for seat_number, player_name in self.table.places.items() if player_name]
        
        # sorted_seats = sorted(occupied_seats, key=lambda x: (x - dealer_buttom) % len(occupied_seats))
        the_game = Game()
        player1 = Player("ilan")
        player2 = Player("zur")
        player3 = Player("oz")
        player4 = Player("tomer")
        player5 = Player("reut")
        player6 = Player("bob")
        player7 = Player("waga")
        player1.add_to_stack(100)
        player2.add_to_stack(100)
        player3.add_to_stack(100)
        player4.add_to_stack(100)
        player5.add_to_stack(100)
        player6.add_to_stack(100)
        player7.add_to_stack(100)
        
        players = [player1 , player2, player3, player4, player5,player6,player7]
        for player in players:
            the_game.add_player(player)
        the_game.start()
