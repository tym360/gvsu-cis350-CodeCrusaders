"""
-Need to find ways to adjust difficulty of words generated
    -Could potentially limit easy to one type of speech or make it possible to generate four-letter words.
    -Easier and medium could potentially exclude "rarer" letter like x, q, etc.
    -Harder could also generate longer words and could always have one of a few different "rarer" letter like x, q, etc.
"""
import wonderwords
from wonderwords import RandomWord

r = RandomWord()


def generate_word(round):
    if round == 1:
        r.word(word_min_length=5, word_max_length=5)
    if round == 2:
        r.word(word_min_length=5, word_max_length=6)
    if round == 3:
        r.word(word_min_length=6, word_max_length=6)
    if round == 4:
        r.word(word_min_length=6, word_max_length=7)
    if round == 5:
        r.word(word_min_length=7, word_max_length=7)
