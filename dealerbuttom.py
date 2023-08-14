# dealerbuttom.py
class Dealerbuttom:
    def __init__(self, position):
        self.position = position

    def forword_position(self, num_of_player):
        if self.position >= num_of_player:
            self.position = 0
        else: self.position +=1

    def get_position(self):
        return self.position
    

    def __str__(self):
        return f" {self.position}"