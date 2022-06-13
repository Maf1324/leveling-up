from random import choice

class Game:
    def __init__(self) -> None:
        self.wins = 0
        self.losses = 0
        self.draw = 0

    def play(self):
        print('Game on!')
        choice_comp = self.comp_choice()
        play_choice = self.player_choice()
        self.compare_choices(choice_comp, play_choice)

    def compare_choices(self, comp, player):
        if comp[0] == player:
            print(f'THAT was a draw! The computer also picked {comp}.')
            self.draw += 1
            return
        
        result = self.check_who_won(comp, player)
        self.final_result(result, comp)
    
    def final_result(self, result, comp):
        # print(f'in final result \n \n\n {result}')
        if result:
            self.wins += 1
        else:
            self.losses += 1
        
        msg = "Win" if result else "Loss"
        print(f"{msg}! The computer chose {comp.title()}.")

    @staticmethod
    def check_who_won(comp, player):
        if player == 'r':
            from logic import rock as imported
            result = imported[comp]
            return result
        if player == 'p':
            from logic import paper as imported
            result = imported[comp]
            return result
        if player == 's':
            from logic import scissors as imported
            result = imported[comp]
            return result
     
    def show_results(self):
        print(f'Wins: {self.wins} / Losses: {self.losses} / Draws: {self.draw}')
  
    def player_choice(self):
        choice = input('[R]ock, [P]aper or [S]cissors -->')
        if choice.lower() not in ['p', 'r', 's']:
            print('Invalid choice')
            return self.player_choice()
        return choice

    @staticmethod
    def comp_choice():
        choices = ['paper', 'rock', 'scissors']
        c_choice = choice(choices)
        return c_choice


if __name__ == "__main__":
    game = Game()
    for i in range(5):
        print(f'Turn {i+1}')
        print()
        game.play()
        print()

    game.show_results()
    