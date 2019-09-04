import random

def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    pass

def get_guessed_word(secret_word, letter_guessed):
    pass

def is_guess_in_word(guess, secret_word):
    pass

def spaceman(secret_word):
    pass


 secret_word = load_word()
 spaceman(load_word())
