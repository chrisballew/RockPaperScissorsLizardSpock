from Player import Player
import random

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        self.chosen_gesture = random.randint(0, 4)
        print(self.chosen_gesture)
        return self.chosen_gesture
    
    