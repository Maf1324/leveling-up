from words import word


def play():
    hidden = word
    if game_result(word):
        print(f"You where right! the world was {hidden}")
        return
    print(f"Ooooh that was bad! The word was {hidden}. Try again later!")
    return


def game_result(word):
    return True if run_guesses(word) else False


def run_guesses(word):
    guesses = []
    for i in range(3):
        new_word = ""
        guess = get_player_guess()
        guesses.append(guess)
        for letter in word.lower():
            if letter in guesses:
                new_word += letter
            else:
                new_word += "*"
        print(new_word)
    if not word_shot(word):
        return False
    return True


def word_shot(word):
    player = input(
        'Time for the real deal. Tell me, what is the hidden word -->')
    # TODO Add a string verification system
    if not verify_answer(player):
        return word_shot(word)
    if player.lower() != word.lower():
        return False
    return True


def verify_answer(answer):
    try:
        if answer.isnumeric():
            raise ValueError
    except ValueError as error:
        print(f'Erro {error}')
        return False
    return answer.strip()


def get_player_guess():
    guess = input('Type one letter --> ')
    if not guess_is_valid(guess):
        print('Invalid guess')
        return get_player_guess()
    return guess.lower()


def guess_is_valid(guess):
    try:
        if guess.isnumeric():
            raise ValueError
        if 0 > len(guess) or len(guess) > 1:
            raise ValueError
        return True
    except ValueError as e:
        print(f'Erro: {e}')
        return False


if __name__ == "__main__":
    play()
