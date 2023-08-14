# player.py
from table import *
from card import *
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stack = 0
        self.curent_in_pot = 0  # Add a new attribute to track chips bet in the current round
        self.still_in_hand = False

    def upd_name(self, name):
         self.name = name

    def get_name(self):
        return self.name
    
    def add_card(self, card):
        self.hand.append(card)

    def reset_hand(self):
        self.hand = []
    
    def get_hand(self):
        return self.hand
    
    def add_to_stack(self,amount):
        self.stack += amount

    def sub_from_stack(self,amount):
        self.stack -= amount

    def get_stack(self):
        return self.stack
    
    def upd_curent_in_pot(self,amount):
        self.curent_in_pot += amount

    def reset_curent_in_pot(self):
        self.curent_in_pot = 0

    def get_curent_in_pot(self):
        return self.curent_in_pot

    def get_still_in_hand(self):
        return self.still_in_hand
    
    def upd_still_in_hand(self):
        self.still_in_hand = not self.still_in_hand
# ----------------------------- actions -------------------------------------------------------------
    
    
    def bet_call_raise(self, amount):
            self.stack -= amount
            self.upd_curent_in_pot(amount)  # Update the chips_bet attribute

    def fold(self):
        self.upd_still_in_hand()

    def check(self):
        print(f"{self.name} checks.")

    def get_action(self, last_bet_size):

        flag = True

        while flag:
            flag = False
            # if is stack smaller last bet he cant raise
            if self.stack + self.curent_in_pot <= last_bet_size:
                if self.stack == 0:
                    # Player is all in, can't make any more bets
                    return "all in"
                else:
                    action = input(f"{self.name}, please choose an action (call/fold): ").lower()
                    if action == "call":
                            return "all in"
                    elif action == "fold":
                        return action
                    else:
                        print("Invalid action. Please choose 'call' or 'fold'.")
                        flag = True
            else:
                # if he is in bb pre flop and no raise before he cant fold
                # or if he in flop/turn/river and no raise before he cant fold
                if last_bet_size == 2 and self.curent_in_pot == 2 or last_bet_size == 0 :
                    action = input(f"{self.name}, please choose an action (check/raise): ").lower()
                    if action in ["check", "raise"]:
                        return action
                    else:
                        print("Invalid action. Please choose 'check' or 'raise'.")
                        flag = True

                else:
                    action = input(f"{self.name}, please choose an action (fold/call/raise): ").lower()
                    if action == "raise":
                        # check if his rais is all in
                        if (self.stack + self.curent_in_pot) < last_bet_size*2:
                            return "all in"
                        else:
                            return action
                    elif action in ["fold", "call"]: 
                        return action
                    else:
                        print("Invalid action. Please choose 'fold' , 'call' or 'raise'.")
                        flag = True

    def __str__(self):
        return f"{self.name} {self.name} {self.name} {self.name} \n (Chips: {self.stack}) \n (Cards: {', '.join(map(str, self.hand))})"
