import tkinter as tk
from tkinter import messagebox
from windows.windows_settings import button_settings
from random import choice, shuffle
from .consts import UPPER_EN, LOWER_EN, NUMBERS, SEPARATORS, SPECIAL_CHARACTERS

class PasswordsGenerator:
    def __init__(self, parent):
        self.window = parent
        self.setup_ui()
        
    def setup_ui(self):    
        self.label = tk.Label(self.window, text='Добро пожаловать в генератор безопасных паролей!', font=('Montserrat', 15))
        self.label.pack(pady=20)
        
        self.label = tk.Label(self.window, text='Выберите опции и нажмите сгенерировать', font=('Arial', 10))
        self.label.pack(pady=20)
        
        # Фрайм-опросник
        frame_check = tk.Frame(self.window, width=150, height=250)
        frame_check.place(relx=0.21, rely=0.585, anchor='center')

        # Используем grid() для позиционирования в одной строке
        self.label_choise = tk.Label(frame_check, text=' Длина пароля:', font=('Arial', 10))
        self.label_choise.grid(row=0, column=0, padx=20, pady=5, sticky='w')

        self.entry_long_pass = tk.Entry(frame_check, width=15)
        self.entry_long_pass.grid(row=0, column=1, pady=5, sticky='ew')
        
        # Заголовок для опций
        self.label_choise = tk.Label(frame_check, text=' Использовать:', font=('Arial', 10))
        self.label_choise.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='w')
        
        # Переменные для чекбоксов
        self.var_upper = tk.BooleanVar()
        self.var_lower = tk.BooleanVar()
        self.var_digits = tk.BooleanVar()
        self.var_separators = tk.BooleanVar()
        self.var_special = tk.BooleanVar()

        # Чекбоксы для опций
        self.check_box_EN_upper = tk.Checkbutton(frame_check, text='Прописные латинские буквы', font=('Arial', 10), variable=self.var_upper)
        self.check_box_EN_upper.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky='w')
        
        self.check_box_EN_lower = tk.Checkbutton(frame_check, text='Строчные латинские буквы', font=('Arial', 10), variable=self.var_lower)
        self.check_box_EN_lower.grid(row=3, column=0, columnspan=2, padx=20, pady=5, sticky='w')
        
        self.check_box_digits = tk.Checkbutton(frame_check, text='Цифры', font=('Arial', 10), variable=self.var_digits)
        self.check_box_digits.grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky='w')
        
        self.check_box_separators = tk.Checkbutton(frame_check, text='Разделители', font=('Arial', 10), variable=self.var_separators)
        self.check_box_separators.grid(row=5, column=0, columnspan=2, padx=20, pady=5, sticky='w')
        
        self.check_box_special = tk.Checkbutton(frame_check, text='Специальные символы', font=('Arial', 10), variable=self.var_special)
        self.check_box_special.grid(row=6, column=0, columnspan=2, padx=20, pady=5, sticky='w')
        
        # Кнопка для генерации пароля
        self.gen_button = button_settings(frame_check, text='Сгенерировать', command=self.generation)
        self.gen_button.grid(row=8, column=0, columnspan=2, sticky='nsew', padx=20)
        
        # Фрейм с результатом генерации
        frame_result = tk.Frame(self.window, width=150, height=250)
        frame_result.place(relx=0.79, rely=0.3, anchor='n')

        self.label_result = tk.Label(frame_result, text='Ваши сгенерированные пароли:', font=('Arial', 10))
        self.label_result.grid(row=0, column=0, padx=20, pady=5, sticky='w')
        
        self.label_result_1 = tk.Label(frame_result, text='1.', font=('Arial', 10))
        self.label_result_1.grid(row=1, column=0, padx=20, pady=5, sticky='w')
        
        self.label_result_2 = tk.Label(frame_result, text='2.', font=('Arial', 10))
        self.label_result_2.grid(row=2, column=0, padx=20, pady=5, sticky='w')
        
        self.label_result_3 = tk.Label(frame_result, text='3.', font=('Arial', 10))
        self.label_result_3.grid(row=3, column=0, padx=20, pady=5, sticky='w')
        
        self.label_result_4 = tk.Label(frame_result, text='4.', font=('Arial', 10))
        self.label_result_4.grid(row=4, column=0, padx=20, pady=5, sticky='w')
        
        self.label_result_5 = tk.Label(frame_result, text='5.', font=('Arial', 10))
        self.label_result_5.grid(row=5, column=0, padx=20, pady=5, sticky='w')
        
        self.label_result_6 = tk.Label(frame_result, text='6.', font=('Arial', 10))
        self.label_result_6.grid(row=6, column=0, padx=20, pady=5, sticky='w')
        
        self.label_result_7 = tk.Label(frame_result, text='7.', font=('Arial', 10))
        self.label_result_7.grid(row=7, column=0, padx=20, pady=5, sticky='w')
        
        # Кнопка для завершения работы программы
        self.stop_button = button_settings(frame_result, text='Выйти', command=self.stop)
        self.stop_button.grid(row=8, column=0, columnspan=2, sticky='nsew', padx=20)
     
     
    def is_digit(self,long_pass):
        return long_pass.isdigit() and int(long_pass) > 0
    
    def generation(self):
        long_pass = self.entry_long_pass.get()
        is_valid_long_pass = self.is_digit(long_pass)
        pass_num = 7
        
        if is_valid_long_pass and (
            self.var_digits.get() or 
            self.var_separators.get() or 
            self.var_lower.get() or
            self.var_upper.get() or 
            self.var_special.get()):
            
            all_chars = ''
            long_pass = int(long_pass)
            
            if self.var_upper.get():
                all_chars += UPPER_EN
            if self.var_lower.get():
                all_chars += LOWER_EN
            if self.var_digits.get():
                all_chars += NUMBERS
            if self.var_separators.get():
                all_chars += SEPARATORS
            if self.var_special.get():
                all_chars += SPECIAL_CHARACTERS
                
            passwords = []
            for _ in range(pass_num):
                pwd = [choice(all_chars) for _ in range(long_pass)]
                shuffle(pwd) # Перемешиваем символы
                passwords.append(''.join(pwd)) # Объединяем символы в строку

            self.label_result_1.configure(text=f'1. {passwords[0]}')      
            self.label_result_2.configure(text=f'2. {passwords[1]}')      
            self.label_result_3.configure(text=f'3. {passwords[2]}')      
            self.label_result_4.configure(text=f'4. {passwords[3]}')      
            self.label_result_5.configure(text=f'5. {passwords[4]}')      
            self.label_result_6.configure(text=f'6. {passwords[5]}')      
            self.label_result_7.configure(text=f'7. {passwords[6]}')      
        else:
            messagebox.showwarning('Предупреждение', 'Неверная длина пароля или не выбрана ни одна опция')    
    
    def stop(self):
        self.window.withdraw()     