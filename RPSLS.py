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
            pass

    def single_or_multiplayer(self):
        print("Press 1 for singleplayer or 2 for multiplayer")
        self.game_mode = input("")
        if self.game_mode == "1":
            print("You dare challenge the computer?!")
            #player 1 is human
            #player 2 is ai

        #elif selfgamemode == 2
            #multiplayer selected
            #player 1 is human
            #player 2 is human

        #else 
            #print whatchu talkin bout willis

