from madlibs import madlib
from utils import formated_input, formated_print


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
        'First, I will ask you for a few words. You can go crazy with then, just try to use the correct "kind" of word, deal?'  # noqa: E501
    )

    # iterate the "needed words" inner dict keys of the madlib
    w_list = []
    for v in madlib['needed_words'].keys():
        word = formated_input(f"A(n) {v}: ").title(
        ) if 'name' in v else formated_input(f"A(n) {v}: ")
        w_list.append(word)
    return w_list


def show_complete_madlib(words):
    formated_print(madlib['title'])
    formated_print(madlib['text'].format(*words))


if __name__ == "__main__":
    play_game()
