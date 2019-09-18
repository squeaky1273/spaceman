from spaceman import is_word_guessed
from spaceman import get_guessed_word
from spaceman import is_guess_in_word

def test_word_guessed():
    secret_word = 'rat'
    assert is_word_guessed(secret_word, 'r') == True 
    assert is_word_guessed(secret_word, 'l') == False

def test_guessed_word():
    secret_word = 'mat'
    letters_guessed = ['m', 'a', 't']
    assert get_guessed_word(secret_word, letters_guessed) == secret_word

def test_guess_in_word():
    secret_word = 'bat'
    assert is_guess_in_word('b', secret_word) == True
    assert is_guess_in_word('s', secret_word) == False
