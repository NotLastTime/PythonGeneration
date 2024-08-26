import tkinter as tk
from tkinter import messagebox
from windows.windows_settings import button_settings
from random import randint
from math import ceil, log2

class GuessNumbersGame:
    def __init__(self, parent):
        self.window = parent
        self.secret_num = None # Загаданное число
        self.max_count = None # Максимальное число попыток
        self.count = None # Количество ходов
        self.setup_ui()
        self.new_game()
        
    def setup_ui(self):
            self.label = tk.Label(self.window, text='Добро пожаловать в числовую угадайку!', font=('Montserrat', 15))
            self.label.pack(pady=20)
            
            self.label = tk.Label(self.window, text='Угадайте число от 1 до 100', font=('Arial', 12))
            self.label.pack(pady=5)
            
            self.still_attempts_left_label = tk.Label(self.window, text='', font=('Arial', 10))
            self.still_attempts_left_label.pack(pady=10)
            
            self.entry = tk.Entry(self.window, width=32)
            self.entry.pack(pady=10)
            
            self.result_label = tk.Label(self.window, text='', font=('Arial', 10))
            self.result_label.pack(pady=10)
            
            self.start_button = button_settings(self.window, text='Проверить', command=self.check_guess)
            self.start_button.pack(pady=5)
            
            self.new_game_batton = button_settings(self.window, text='Новая игра', command=self.new_game)
            self.new_game_batton.pack(pady=5)

            self.quit_game_batton = button_settings(self.window, text='Выйти', command=self.quit_game)
            self.quit_game_batton.pack(pady=5)
    
    def sec_gen(self):
        return randint(1, 100)
    
    def is_valid(self, s):
        return s.isdigit() and 1 <= int(s) <= 100
    
    # Запускаем новую игру
    def new_game(self):
        self.secret_num = self.sec_gen()         
        self.max_count = ceil(log2(100+1))
        self.count = 0
        self.result_label.configure(text='') # Очищаем результат
        self.still_attempts_left_label.configure(text=f'У Вас осталось {self.max_count} попыток')
        self.entry.configure(state=tk.NORMAL) # Включаем строку ввода
        self.start_button.config(state=tk.NORMAL) # Включаем кнопку
        
    def check_guess(self):
        num = self.entry.get() # Получаем число от пользователя
        
        if self.is_valid(num):
            num = int(num)
            self.count += 1
            
            if num == self.secret_num:
                new_text = f'Вы угадали, поздравляем! Затрачено попыток: {self.count}'
                self.disable_game()
            elif num < self.secret_num:
                new_text = 'Ваше число меньше загаданного, попробуйте еще разок'
            elif num > self.secret_num:
                new_text = 'Ваше число больше загаданного, попробуйте еще разок'
                
            # Обновляем информацию в лейблах
            self.result_label.configure(text=new_text)
            self.still_attempts_left_label.configure(text=f'Осталось попыток: {self.max_count - self.count}')
            
            # Проверка на исчерпание попыток
            if self.count >= self.max_count and num != self.secret_num:
                self.result_label.configure(text=f'Вы исчерпали все попытки. Загаданное число: {self.secret_num}')
                self.disable_game()
        else:
            # Если введено недействительное число
            #self.result_label.configure(text='А может быть все-таки введем целое число от 1 до 100?')
            messagebox.showwarning("Предупреждение", "А может быть все-таки введем целое число от 1 до 100?")
    
    def disable_game(self):
        self.entry.configure(state=tk.DISABLED) # Отключаем ввод             
        self.start_button.configure(state=tk.DISABLED) # Отключаем кнопку
    
    def quit_game(self):
        self.window.withdraw()          