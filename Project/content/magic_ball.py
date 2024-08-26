import tkinter as tk
from windows.windows_settings import button_settings
from random import choice
from .consts import ANSWERS

class MagicBallGame:
    def __init__(self, parent):
        self.window = parent
        self.setup_ui()
    
    def setup_ui(self):
        self.label = tk.Label(self.window, text='Добро пожаловать, путник!', font=('Montserrat', 15))
        self.label.pack(pady=20)
        
        self.label = tk.Label(self.window, text='Задайте вопрос и я на него отвечу', font=('Arial', 10))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.window, width=32)
        self.entry.pack(pady=10)
        
        self.answer_label = tk.Label(self.window, text='', font=('Arial', 10))
        self.answer_label.pack(pady=0, padx=10)
        
        self.question_button = button_settings(self.window, text='Спросить', command=self.set_question)
        self.question_button.pack(pady=5)
       
        self.button_stop = button_settings(self.window, text='Выйти', command=self.stop_button)
        self.button_stop.pack(pady=5)
    
    def set_question(self):
        question = self.entry.get().lower()
        
        if question == '':
            self.answer_label.configure(text='Пожалуйста, задайте вопрос.')
        elif question[-1] != '?':
            self.answer_label.configure(text='Я не уверен, что это вопрос. В конце вопроса ставится знак "?"\nПопробуйте еще раз')
        else:
            response = choice(ANSWERS)
            self.answer_label.configure(text=response)
            self.entry.delete(0, tk.END) # Очищаем строку ввода  
    
    def stop_button(self):
        self.window.withdraw()      