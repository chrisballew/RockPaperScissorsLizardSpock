from Player import Player

class human(Player):
    def __init__(self):
        super().__init__()
        self.gesture

    def choose_gesture(self):
        self.chosen_gesture = self.gesture[0:4]
        user_input = (input('Pick a gesture: '))
        user_input = user_input.lower
        if user_input == self.gesture[0]:
            print("You chose rock.")
            return self.gesture[0]
        
        elif user_input == self.gesture[1]:
            print("You chose paper.")
            return self.gesture[1]
        
        elif user_input == self.gesture[2]:
            print("You chose scissors.")
            return self.gesture[2]
        
        elif user_input == self.gesture[3]:
            print("You chose lizard.")
            return self.gesture[3]
        
        elif user_input == self.gesture[4]:
            print("You chose Spock.")
            return self.gesture[4]
        
        else:
            print("Ya dun goofed! Option is not valid.")