import tkinter as tk
from tkinter import messagebox
from windows.windows_settings import button_settings
from random import choice
from .consts import WORDS, UPPER_RU

class GuessWordGame:
    def __init__(self, parent):
        self.window = parent
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.window, text='Добро пожаловать в Угадайку слов!', font=('Montserrat', 15))
        self.label.pack(pady=20)
        
        self.canvas = tk.Canvas(self.window, width=150, height=150, background='white')
        self.canvas.pack(pady=20)
        
        self.parts_drawn = 0  # Изначально ни одна часть тела не нарисована
        self.max_parts = 6  # Максимальное количество частей висельника
        
        self.label_secret_word = tk.Label(self.window, text='', font=('Arial', 12))
        self.label_secret_word.pack(pady=5)

        self.word = choice(WORDS).upper()  # Загаданное слово
        self.guessed_word = ['_' for _ in self.word]  # Загаданное слово с заменой букв на "_"
        
        self.word_label = tk.Label(self.window, text=' '.join(self.guessed_word), font=('Arial', 10))
        self.word_label.pack(pady=25)
        
        self.start_button = button_settings(self.window, text='Начать игру', command=self.start_game)
        self.start_button.place(relx=0.5, rely=0.75, anchor='center')
        
        frame_user_entry = tk.Frame(self.window, width=100, height=20)
        frame_user_entry.place(relx=0.5, rely=0.6, anchor='n')
        
        self.label = tk.Label(frame_user_entry, text='Введите букву:', font=('Arial', 10))
        self.label.grid_forget()  # Скрываем пользовательский ввод
        
        self.entry_alpha = tk.Entry(frame_user_entry, width=20)
        self.entry_alpha.grid_forget()  # Скрываем пользовательский ввод
        
        self.try_button = button_settings(self.window, text='Попытаться', command=self.try_guess)
        self.try_button.place_forget()  # Скрываем кнопку "Попытаться"
        
        self.stop_button = button_settings(self.window, text='Выйти', command=self.stop_game)
        self.stop_button.place(relx=0.5, rely=0.83, anchor='center')
        
        self.new_game_button = button_settings(self.window, text='Новая игра', command=self.new_game)
        self.new_game_button.place_forget()  # Скрываем кнопку "Новая игра" до завершения текущей

        self.draw_hangman_base()  # Вызов отрисовки основы виселицы сразу при запуске UI
    
    def start_game(self):
        self.label_secret_word.configure(text=f'Я загадал слово из {len(self.word)} букв. Попробуйте угадать.')
        self.start_button.place_forget()  # Скрываем кнопку "Начать игру"
        self.try_button.place(relx=0.5, rely=0.75, anchor='center')  # Показываем кнопку "Попытаться"
        # Показываем пользовательский ввод
        self.label.grid(row=0, column=0, sticky='e')
        self.entry_alpha.grid(row=0, column=2, columnspan=2, sticky='e')
        
    def try_guess(self):
        guess = self.entry_alpha.get().upper()
        if len(guess) == 1 and guess.isalpha() and guess in UPPER_RU:
            if guess in self.word:
                self.update_word(guess)
            else:
                self.draw_hangman()
                
            self.word_label.configure(text=' '.join(self.guessed_word))                   
        else:
            messagebox.showwarning('Предупреждение', 'Вводите по одной букве. Используйте кириллицу.')
        
        self.entry_alpha.delete(0, tk.END)
        
        # Проверка на завершение игры
        if "_" not in self.guessed_word:
            self.word_label.config(text=f"Вы угадали слово: {self.word}!")
            self.end_game()
        elif self.parts_drawn >= self.max_parts:
            self.word_label.config(text=f"Вы проиграли! Слово было: {self.word}")
            self.end_game()
        
    def draw_hangman_base(self):
        '''Рисуется так:
            create_line(x1, y1, x2, y2, width=5)
            x1, y1: Координаты начала линии (первой точки)
            x2, y2: Координаты конца линии (второй точки)
            width=5: Толщина линии (по умолчанию 5 пикселей)
            Координаты считаются от левого верхнего угла'''
        self.canvas.create_line(30, 135, 125, 135, width=5)  # Основание
        self.canvas.create_line(75, 135, 75, 25, width=5)  # Столб
        self.canvas.create_line(75, 25, 125, 25, width=5)  # Верхняя перекладина
        self.canvas.create_line(125, 25, 125, 45, width=5)  # Веревка
        
    def draw_hangman(self):
        if self.parts_drawn == 0:
            self.canvas.create_oval(110, 45, 140, 75, width=5)  # Голова
        elif self.parts_drawn == 1:
            self.canvas.create_line(125, 75, 125, 110, width=5)  # Туловище
        elif self.parts_drawn == 2:
            self.canvas.create_line(125, 85, 110, 95, width=5)  # Левая рука
        elif self.parts_drawn == 3:
            self.canvas.create_line(125, 85, 140, 95, width=5)  # Правая рука
        elif self.parts_drawn == 4:
            self.canvas.create_line(125, 110, 110, 125, width=5)  # Левая нога
        elif self.parts_drawn == 5:
            self.canvas.create_line(125, 110, 140, 125, width=5)  # Правая нога
        self.parts_drawn += 1                
    
    def update_word(self, guess):
        correct_guess = False
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.guessed_word[i] = guess
                correct_guess = True
        self.word_label.config(text=" ".join(self.guessed_word))
    
    def end_game(self):
        # Завершение игры: блокировка ввода и отображение кнопки новой игры
        self.try_button.place_forget()  # Скрываем кнопку "Попытаться"
        self.label.grid_forget()  # Скрываем текст "Введите букву"
        self.entry_alpha.grid_forget()  # Скрываем поле ввода
        
        self.new_game_button.place(relx=0.5, rely=0.75, anchor='center')  # Показываем кнопку "Новая игра"

    def new_game(self):
        # Сбрасываем игру и начинаем новую
        self.canvas.delete("all")  # Очистить канвас
        self.draw_hangman_base()  # Нарисовать базу виселицы
        self.parts_drawn = 0  # Сброс количества нарисованных частей висельника
        
        self.word = choice(WORDS).upper()  # Случайно выбираем новое слово
        self.guessed_word = ['_' for _ in self.word]  # Сбрасываем угаданные буквы
        
        self.word_label.config(text=' '.join(self.guessed_word))  # Обновляем отображение слова
        self.label_secret_word.config(text=f'Я загадал слово из {len(self.word)} букв. Попробуйте угадать.')  # Обновляем текст с количеством букв
        
        self.new_game_button.place_forget()  # Скрываем кнопку "Новая игра"
        self.start_button.place(relx=0.5, rely=0.75, anchor='center')  # Снова показываем кнопку "Начать игру"

    def stop_game(self):
        self.window.withdraw()
