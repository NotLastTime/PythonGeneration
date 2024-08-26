import tkinter as tk
from windows.windows_settings import button_settings
from windows.functions import open_and_close_game

class Choice:
    def __init__(self, parent):
        self.window = parent
        self.setup_ui()
        
    def setup_ui(self):
        self.label = tk.Label(self.window, text='Выберите игру:', font=('Montserrat', 15))
        self.label.pack(pady=20)
        
        self.button_gn = button_settings(self.window, text='Числовая угадайка', command=lambda: open_and_close_game(self.window, game_name='guess_number'))
        self.button_gn.pack(pady=5)
        
        self.button_mg = button_settings(self.window, text='Магический шар', command=lambda: open_and_close_game(self.window, game_name='magic_ball'))
        self.button_mg.pack(pady=5)
        
        self.button_pg = button_settings(self.window, text='Генератор паролей', command=lambda: open_and_close_game(self.window, game_name='pass_gen'))
        self.button_pg.pack(pady=5)
        
        self.button_cc = button_settings(self.window, text='Шифр Цезаря', command=lambda: open_and_close_game(self.window, game_name='caesar_cipher'))
        self.button_cc.pack(pady=5)
        
        self.button_gw = button_settings(self.window, text='Угадайка слов', command=lambda: open_and_close_game(self.window, game_name='guess_word'))
        self.button_gw.pack(pady=5)
        
        self.button_cg = button_settings(self.window, text='Калькулятор систем счисления', command=lambda: open_and_close_game(self.window, game_name='calculator'))
        self.button_cg.pack(pady=5)
        
        self.button_cancel = tk.Button(self.window,
                                       text='Выход', font=('Arial', 10),
                                       background='lightblue', activebackground='lightblue',
                                       width=10,
                                       command=quit)
        self.button_cancel.pack(pady=20)
      
        