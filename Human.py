from Player import Player

class human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.chosen_gesture = self.gesture[0:4]
        user_input = int(input('Pick a gesture'))
        print(self.choose_gesture)