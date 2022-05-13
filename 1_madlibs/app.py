from madlibs import madlib
from utils import formated_input, formated_print


# Let's play?
def ask_play_game():
    invalid_msg = 'Invalid answer! Use "y" or "n"'
    play = formated_input("Wanna play a game? [y/n] --> ")
    try:
        answer = play.strip().lower()
    except TypeError as e:
        formated_print(invalid_msg)

    if answer == "n":
        formated_print('Well see you some other time!')
        return
    if answer == "y":
        formated_print("Awsome!")
        return play_game()

    formated_print(invalid_msg)
    ask_play_game()


# game started!
def play_game():
    formated_print('Game started!')
    words = get_player_words()
    formated_print('And the final result is...')
    show_complete_madlib(words)
    formated_print('The End!')


# let the code do the hardwork
def get_player_words():
    formated_print(
        'First, I will ask you for a few words. You can go crazy with then, just try to use the correct "kind" of word, deal?'
    )
    # iterate the "needed words" inner dict keys of the madlib
    return [
        formated_input(f"A(n) {v}: ") for v in madlib['needed_words'].keys()
    ]


# Show the finished madlib
def show_complete_madlib(words):
    formated_print(madlib['title'])
    formated_print(madlib['text'].format(*words))


if __name__ == "__main__":
    ask_play_game()
