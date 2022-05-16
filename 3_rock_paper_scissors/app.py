from random import choice


def play():
    print('Game on!')
    choice_comp = comp_choice()
    play_choice = player_choice()
    check_who_won(choice_comp, play_choice)


def check_who_won(comp, player):
    if comp[0] == player:
        print('THAT was a draw!')
        return

    if player == 'r':
        from logic import rock as imported
        result = imported[comp]
    if player == 'p':
        from logic import paper as imported
        result = imported[comp]
    if player == 's':
        from logic import scissors as imported
        result = imported[comp]

    print(f"{result}! The computer chose {comp.title()}.")


def player_choice():
    choice = input('[R]ock, [P]aper or [S]cissors -->')
    if choice.lower() not in ['p', 'r', 's']:
        print('Invalid choice')
        return player_choice()
    return choice


def comp_choice():
    choices = ['paper', 'rock', 'scissors']
    c_choice = choice(choices)
    return c_choice


if __name__ == "__main__":
    while True:
        play()
