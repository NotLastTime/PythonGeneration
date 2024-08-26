import tkinter as tk
from tkinter import messagebox
from windows.windows_settings import button_settings
from .consts import UPPER_EN, UPPER_RU, LOWER_EN, LOWER_RU

class CaesarCipherGame():
    def __init__(self, parent):
        self.window = parent
        self.setup_ui()
        
    def setup_ui(self):
        self.label = tk.Label(self.window, text='Добро пожаловать в шифратор Цезаря', font=('Montserrat', 15))
        self.label.pack(pady=20)
        
        self.label = tk.Label(self.window, text='Введите текст и выберите опции', font=('Arial', 12))
        self.label.pack(pady=10)
        
        self.entry_str = tk.Entry(self.window, width=32)
        self.entry_str.pack(pady=5)
        
        # Переменная для радиокнопок
        self.var_crypt = tk.StringVar(value='None')
        self.var_direction = tk.StringVar(value='None')
              
        # Создание фрейма для размещения радиокнопок шифра
        frame_crypt_radio = tk.Frame(self.window)
        frame_crypt_radio.pack(pady=5)  # Вы можете добавить отступы по вертикали, если нужно

        # Радиокнопки
        self.encrypt_radio = tk.Radiobutton(frame_crypt_radio, text='Зашифровать', font=('Arial', 10), value='encrypt', variable=self.var_crypt)
        self.encrypt_radio.pack(side=tk.LEFT, padx=5)  # Разместить слева с небольшим отступом

        self.decrypt_radio = tk.Radiobutton(frame_crypt_radio, text='Расшифровать', font=('Arial', 10), value='decrypt', variable=self.var_crypt)
        self.decrypt_radio.pack(side=tk.LEFT, padx=5)  # Разместить слева от предыдущего элемента
        
        # Создание фрейма для направления
        frame_crypt_direction = tk.Frame(self.window)
        frame_crypt_direction.pack(pady=5)

        self.label_direction = tk.Label(frame_crypt_direction, text='Направление:', font=('Arial', 10))
        self.label_direction.pack(side=tk.LEFT, padx=5)
        
        self.direction_radio_left = tk.Radiobutton(frame_crypt_direction, text='Влево', font=('Arial', 10), value='left', variable=self.var_direction)
        self.direction_radio_left.pack(side=tk.LEFT, padx=5)  # Разместить слева с небольшим отступом

        self.direction_radio_right = tk.Radiobutton(frame_crypt_direction, text='Вправо', font=('Arial', 10), value='right', variable=self.var_direction)
        self.direction_radio_right.pack(side=tk.LEFT, padx=5)  # Разместить слева от предыдущего элемента
 
        # Создание фрейма для шага
        frame_crypt_step = tk.Frame(self.window)
        frame_crypt_step.pack(pady=10)

        self.label_step = tk.Label(frame_crypt_step, text='Смещение:', font=('Arial', 10))
        self.label_step.pack(side=tk.LEFT, padx=5) 

        self.entry_step = tk.Entry(frame_crypt_step, width=15)
        self.entry_step.pack(side=tk.LEFT, padx=5)
        
        self.result_label = tk.Label(self.window, text='', font=('Arial', 12))
        self.result_label.pack(pady=5)

        self.crypt_button = button_settings(self.window, text='Выполнить', command=self.is_valid_options)
        self.crypt_button.pack(pady=5)
        
        self.quit_game_batton = button_settings(self.window, text='Выйти', command=self.quit_game)
        self.quit_game_batton.pack(pady=5)
        
    def is_digit(self, step):
        return step.isdigit()
    
    def is_valid_options(self):
        string = self.entry_str.get()
        step = self.entry_step.get()
        
        if self.var_crypt.get() == 'None':
            messagebox.showwarning("Предупреждение", "Выберите действие: зашифровать или расшифровать.")
        elif self.var_direction.get() == 'None':
            messagebox.showwarning("Предупреждение", "Укажите направление шифрования.")
        elif not self.is_digit(step):
            messagebox.showwarning("Предупреждение", "Укажите корректное смещение.")
        else:
            lang = self.is_valid_string(string)
            self.crypt(string, step, lang)
    
    def is_valid_string(self, string):
        string = string.lower()
        latin = set(LOWER_EN)
        cyrillyc = set(LOWER_RU)
        
        latin_count = sum(1 for char in string if char in latin)
        cyrillyc_count = sum(1 for char in string if char in cyrillyc)
        
        if latin_count == 0 and cyrillyc_count > 0:
            return 1
        elif latin_count > 0 and cyrillyc_count == 0:
            return 0
        else:
            return -1
        
    def crypt(self, string, step, lang):
        result_str = []
        step = int(step)
        
        if lang == -1:
            messagebox.showwarning("Предупреждение", "Пустая строка или в тексте буквы разных алфавитов")
        else:
            if lang == 1:
                upper = UPPER_RU
                lower = LOWER_RU
            else:
                upper = UPPER_EN
                lower = LOWER_EN

            n = len(upper)    
                
        # Если расшифровываем меняем знак сдвига
        if self.var_crypt.get() == 'decrypt':
            step = -step        
        
        for char in string:
            if char.isalpha():
                if char.isupper():
                    alphabet = upper
                else:
                    alphabet = lower
                idx = alphabet.index(char)
                new_idx = (idx + step) % n
                result_str.append(alphabet[new_idx])    
            else:
                result_str.append(char) # Добавляем символы, которые не являются буквами, без изменений
        
        self.result_label.configure(text=''.join(result_str))
                
    def quit_game(self):
        self.window.withdraw()