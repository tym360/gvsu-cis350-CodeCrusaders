import wonderwords
from wonderwords import RandomWord

r = RandomWord()



def generate_word():
    return r.word(word_min_length=5, word_max_length=5)

#print(generate_word())
