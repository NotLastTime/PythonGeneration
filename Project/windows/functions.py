from .guess_number_window import create_guess_window
from .magic_ball_window import create_magic_window
from .caesar_cipher_window import create_caesar_game_window
from .passwods_gen_window import create_pass_gen_window
from .calculator_window import create_calculator_window
from .guess_words_window import create_guess_word_window

def open_guess_number(choice_window):
    create_guess_window(choice_window)

def open_magic_ball(choice_window):
    create_magic_window(choice_window) 
    
def open_caesar_cipher(choice_window):
    create_caesar_game_window(choice_window)
    
def open_pass_gen(choice_window):
    create_pass_gen_window(choice_window)
    
def open_calculator(choice_window):
    create_calculator_window(choice_window)

def open_guess_word(choice_window):
    create_guess_word_window(choice_window)

def open_and_close_game(choice_window, game_name):
    game_function = {
        'guess_number': open_guess_number,
        'magic_ball': open_magic_ball,
        'caesar_cipher': open_caesar_cipher,
        'pass_gen': open_pass_gen,
        'calculator': open_calculator,
        'guess_word' : open_guess_word
    }
    
    if game_name in game_function:
        game_function[game_name](choice_window)

