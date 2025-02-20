"""
-Need to find ways to adjust difficulty of words generated
    -Could potentially limit easy to one type of speech or make it possible to generate four-letter words.
    -Easier and medium could potentially exclude "rarer" letter like x, q, etc.
    -Harder could also generate longer words and could always have one of a few different "rarer" letter like x, q, etc.
"""
import wonderwords
from wonderwords import RandomWord

r = RandomWord()


def generate_word_easy():
    return r.word(include_parts_of_speech=["nouns"], word_min_length=5, word_max_length=5)


def generate_word_medium():
    return r.word(word_min_length=5, word_max_length=5)


def generate_word_hard():
    return r.word(word_min_length=5, word_max_length=6)
