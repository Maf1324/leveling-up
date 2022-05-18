from random import choice

string = "Hunched Afogar Assistente Copo Intrometido Percentagem Movimento Emboscada Loiro Asilo"  # noqa E501
words = string.split(" ")


def get_word(words):
    return choice(words)


word = get_word(words)
