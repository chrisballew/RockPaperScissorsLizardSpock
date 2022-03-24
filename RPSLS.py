from Player import Player
from Human import human
from AI import AI

class Game:
    def __init__(self):
        self.player_1 = human("Chris")
        self.player_2 = AI("R2-D2")

    def run_game():
        pass

    def display_welcome():
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        rules_input = input(print("Do you know the rules? Press 'n' for the rules. Otherwise, press any key to continue: "))
        if rules_input == ("n"):
            print("Here are the rules of the game!")
            print("Rock crushes Scissors")
            print("Scissors cuts Paper")
            print("Paper covers Rock")
            print("Rock crushes Lizard")
            print("Lizard poisons Spock")
            print("Spock smashes Scissors")
            print("Scissors decapitates Lizard")
            print("Lizard eats Paper")
        else:
            return(rules_input)

    def single_or_multiplayer():
        print("Would you like to play against the computer, or against a friend?")

        
