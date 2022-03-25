from Player import Player
from Human import human
from AI import AI

class Game:
    def __init__(self):
        pass

    def run_game(self):
        self.player_1 = human("Chris")
        self.player_2 = AI
        self.display_welcome()
        self.single_or_multiplayer()
        while (self.player_1.player_score < 2 and self.player_2.player_score < 2):
            self.player_1.choose_gesture()
            self.player_2.choose_gesture()
            self.referee()
            self.display_winner()

    def display_welcome(self):
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
            print("Spock vaporizes Rock")
        else:
            return(rules_input)

    def single_or_multiplayer(self):
        print("Press 1 for singleplayer or 2 for multiplayer")
        self.game_mode = input("")
        if self.game_mode == "1":
            print("You dare challenge the computer?!")    

        elif self.game_mode == "2":
            print("You have selected multiplayer!")
            self.player_2 = human("Deondre")

        else:
            print("whatchu talkin bout willis?")

    def display_winner(self):
        if (self.player_1.player_score == 2):
            print(f'{self.player_1} wins the game!')

        elif (self.player_2.player_score == 2):
            print(f'{self.player_2} wins the game!')

    def referee(self):

        if self.player_1.chosen_gesture == 'rock':
            if self.player_2.chosen_gesture == 'rock':
                print('Tie')
            
            elif self.player_2.chosen_gesture == 'paper':
                self.player_2.player_score += 1
                print(f'paper covers rock, {self.player_2} wins')
            
            elif self.player_2.chosen_gesture == 'scissors':
                self.player_1.player_score += 1
                print(f'rock crushes scissors, {self.player_1} wins')

            elif self.player_2.chosen_gesture == 'lizard':
                self.player_1.player_score += 1
                print(f'rock crushes lizard, {self.player_1} wins')
            
            elif self.player_2.chosen_gesture == 'spock':
                self.player_2.player_score +=1
                print(f'spock vaporizes rock, {self.player_2} wins')

        
        if self.player_1.chosen_gesture == 'paper':
            if self.player_2.chosen_gesture == 'rock':
                self.player_2.player_score += 1
                print(f'paper covers rock, {self.player_1} wins')
            
            elif self.player_2.chosen_gesture == 'paper':
                print('Tie') 

            elif self.player_2.chosen_gesture == 'scissors':
                self.player_2.player_score += 1
                print(f'scissors cut paper, {self.player_2} wins')

            elif self.player_2.chosen_gesture == 'lizard':
                self.player_2.player_score += 1
                print(f'lizard eats paper, {self.player_2} wins')
            
            elif self.player_2.chosen_gesture == 'spock':
                self.player_1.player_score += 1
                print(f'paper disproves spock, {self.player_1} wins')
        
        
        if self.player_1.chosen_gesture == 'scissors':
            if self.player_2.chosen_gesture == 'rock':
                self.player_2.player_score += 1
                print(f'rock crushes scissors, {self.player_2} wins')
            
            elif self.player_2.chosen_gesture == 'scissors':
                print('Tie') 

            elif self.player_2.chosen_gesture == 'paper':
                self.player_1.player_score += 1
                print(f'scissors cut paper {self.player_1} wins')

            elif self.player_2.chosen_gesture == 'lizard':
                self.player_1.player_score += 1
                print(f'scissors decapitates lizard {self.player_1} wins')
            
            elif self.player_2.chosen_gesture == 'spock':
                self.player_2.player_score += 1
                print(f'spock smashes scissors {self.player_2} wins')
        

        if self.player_1.chosen_gesture == 'lizard':
            if self.player_2.chosen_gesture == 'rock':
                self.player_2.player_score += 1
                print(f'rock crushes lizard {self.player_2} wins')
            
            elif self.player_2.chosen_gesture == 'lizard':
                print('Tie') 

            elif self.player_2.chosen_gesture == 'scissors':
                self.player_2.player_score += 1
                print(f'scissors decapitates lizard {self.player_2} wins')

            elif self.player_2.chosen_gesture == 'paper':
                self.player_1.player_score += 1
                print(f'lizard eats paper {self.player_1} wins')
            
            elif self.player_2.chosen_gesture == 'spock':
                self.player_1.player_score += 1
                print(f'lizard poisons spock {self.player_1} wins')
        

        if self.player_1.chosen_gesture == 'spock':
            if self.player_2.chosen_gesture == 'rock':
                self.player_1.player_score += 1
                print(f'spock vaporizes rock {self.player_1} wins')
            
            elif self.player_2.chosen_gesture == 'spock':
                print('Tie') 

            elif self.player_2.chosen_gesture == 'paper':
                self.player_2.player_score += 1
                print(f'paper disproves spock {self.player_2} wins')

            elif self.player_2.chosen_gesture == 'scissors':
                self.player_1.player_score += 1
                print(f'spock smashes scissors {self.player_1} wins')
            
            elif self.player_2.chosen_gesture == 'lizard':
                self.player_2.player_score += 1
                print(f'lizard poisons spock {self.player_2} wins')