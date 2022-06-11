from random import randint


class Game:
    def __init__(self) -> None:
        print("welcome to guess the number!")

        self.difficulty = self.pick_difficulty()

    def play(self) -> bool:
        comp_number = self.get_comp_number(self.difficulty)
        player_number = self.get_player_number(self.difficulty)
        win = self.check_choices(comp_number, player_number)
        if win:
            print(f"Nice you got it right the number was {comp_number}!")
            return True
        print(
            f'Well...that was bad, the number was {comp_number}. Maybe if you try again!')  # noqa: E501
        return False

    def pick_difficulty(self):
        print("Choose the difficulty of the game...")
        print()
        print('Easy [1-10]', 'Medium [1-50]', 'Hard [1-100]')
        choice = input('Pick your poison ["E", "M" or "H"] --> ')
        difficulty = self.clean_choice(choice)

        if difficulty == "e":
            return 10
        elif difficulty == "m":
            return 50
        elif difficulty == "h":
            return 100

    def clean_choice(self, choice):
        try:
            choice = choice.lower().strip()
            if choice not in ["e", "m", "h"]:
                raise TypeError
        except TypeError as e:
            print(f"Erro {e}")
            print('Invalid option...')
            return self.clean_choice(input('Pick your poison ["E", "M" or "H"] --> '))
        return choice

    def get_comp_number(self, max=10):
        print(f"The computer chose a number, it's beetween 1 and {max}!")
        return randint(1, max)

    def get_player_number(self, max=10):
        try:
            number = input(f'Pick a number beetween 1 and {max} --> ')
            number = int(number.strip())
            if number > max or number < 0:
                raise ValueError
        except ValueError:
            print(
                f'Invalid value, try again with a number beetween 1 and {max}')
            return self.get_player_number(max)

        return number

    def check_choices(self, comp_choice, player_choice):
        if comp_choice != player_choice:
            return False
        return True


if __name__ == "__main__":
    game = Game()
    while True:
        print("----------------------------------------------------")
        print()
        game.play()
        print()
