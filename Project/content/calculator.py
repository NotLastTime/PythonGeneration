import tkinter as tk
from tkinter import messagebox
from windows.windows_settings import button_settings

class Calclator:
    def __init__(self, parent):
        self.window = parent
        self.setup_ui()
        
    def setup_ui(self):    
        self.label = tk.Label(self.window, text='Добро пожаловать в калькулятор систем счисления!', font=('Montserrat', 15))
        self.label.pack(pady=20)
        
        frame_label_num = tk.Frame(self.window, width=200)
        frame_label_num.place(relx=0.5, rely=0.17, anchor='center')
        
        self.label_num = tk.Label(frame_label_num, text='Введите число > 0', font=('Arial', 10))
        self.label_num.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        
        self.entry_num = tk.Entry(frame_label_num, width=50)
        self.entry_num.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky='e')

        # Переменные для кнопок
        self.var_original = tk.StringVar(value='None')
        self.var_finaly = tk.StringVar(value='None')

        # Фрейм оригинальной системы
        frame_original_system = tk.Frame(self.window, width=100, height=200)
        frame_original_system.place(relx=0.23, rely=0.4, anchor='center')

        self.label_original = tk.Label(frame_original_system, text='Его система счисления', font=('Arial', 10))
        self.label_original.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        self.original_binary_radio = tk.Radiobutton(frame_original_system, text='Двоичная', font=('Arial', 10), variable=self.var_original, value='binary')
        self.original_binary_radio.grid(row=1, column=0, columnspan=2, sticky='w')
        
        self.original_ternary_radio = tk.Radiobutton(frame_original_system, text='Троичная', font=('Arial', 10), variable=self.var_original, value='ternary')
        self.original_ternary_radio.grid(row=2, column=0, columnspan=2, sticky='w')
        
        self.original_octal_radio = tk.Radiobutton(frame_original_system, text='Восьмеричная', font=('Arial', 10), variable=self.var_original, value='octal')
        self.original_octal_radio.grid(row=3, column=0, columnspan=2, sticky='w')
        
        self.original_decimal_radio = tk.Radiobutton(frame_original_system, text='Десятичная', font=('Arial', 10), variable=self.var_original, value='decimal')
        self.original_decimal_radio.grid(row=4, column=0, columnspan=2, sticky='w')
        
        self.original_hex_radio = tk.Radiobutton(frame_original_system, text='Шестнадцатеричная', font=('Arial', 10), variable=self.var_original, value='hex')
        self.original_hex_radio.grid(row=5, column=0, columnspan=2, sticky='w')
        
        # Фрейм финальной системы
        frame_final_system = tk.Frame(self.window, width=100, height=200)
        frame_final_system.place(relx=0.78, rely=0.24, anchor='n')

        self.label_final = tk.Label(frame_final_system, text='Переводим в', font=('Arial', 10))
        self.label_final.grid(row=0, column=0, pady=5, sticky='w')
        
        # Финальные кнопки
        self.final_binary_radio = tk.Radiobutton(frame_final_system, text='Двоичная', font=('Arial', 10), variable=self.var_finaly, value='binary')
        self.final_binary_radio.grid(row=1, column=0, columnspan=2, sticky='w')
        
        self.final_ternary_radio = tk.Radiobutton(frame_final_system, text='Троичная', font=('Arial', 10), variable=self.var_finaly, value='ternary')
        self.final_ternary_radio.grid(row=2, column=0, columnspan=2, sticky='w')
        
        self.final_octal_radio = tk.Radiobutton(frame_final_system, text='Восьмеричная', font=('Arial', 10), variable=self.var_finaly, value='octal')
        self.final_octal_radio.grid(row=3, column=0, columnspan=2, sticky='w')
        
        self.final_decimal_radio = tk.Radiobutton(frame_final_system, text='Десятичная', font=('Arial', 10), variable=self.var_finaly, value='decimal')
        self.final_decimal_radio.grid(row=4, column=0, columnspan=2, sticky='w')
        
        self.final_hex_radio = tk.Radiobutton(frame_final_system, text='Шестнадцатеричная', font=('Arial', 10), variable=self.var_finaly, value='hex')
        self.final_hex_radio.grid(row=5, column=0, columnspan=2, sticky='w')
        
        # Результат
        frame_result = tk.Frame(self.window, width=100, height=20)
        frame_result.place(relx=0.5, rely=0.6, anchor='n')
        
        self.result_label = tk.Label(frame_result, text='Результат:', font=('Arial', 10))
        self.result_label.grid(row=0, column=0, sticky='e')
        
        self.result = tk.Label(frame_result, text='', font=('Arial', 10))
        self.result.grid(row=0, column=1, columnspan=2, sticky='e')

        # Упаравляющие кнопки
        self.result_button = button_settings(self.window, text='Перевести', command=self.translate)
        self.result_button.place(relx=0.3, rely=0.7)
        
        self.close_button = button_settings(self.window, text='Выйти', command=self.quit_game)
        self.close_button.place(relx= 0.3, rely=0.77)
        
    def convert_number(self, num, from_base, to_base):
        delcimal_value = int(num, from_base)
        
        if to_base == 10:
            return str(delcimal_value)
        if to_base == 2:
            return bin(delcimal_value)[2:]
        if to_base == 8:
            return oct(delcimal_value)[2:]
        if to_base == 16:
            return hex(delcimal_value)[2:].upper()
    
    def translate(self):
        num = self.entry_num.get()

        from_base = {
            'binary' : 2,
            'ternary' : 3,
            'octal' : 8,
            'decimal' : 10,
            'hex' : 16
        }.get(self.var_original.get())
        
        to_base = {
            'binary' : 2,
            'ternary' : 3,
            'octal' : 8,
            'decimal' : 10,
            'hex' : 16
        }.get(self.var_finaly.get())
        
        if from_base is None or to_base is None:
            messagebox.showwarning('Предупреждение', 'Укажите систему счисления.')
            return

        result = self.convert_number(num, from_base, to_base)
                
        self.result.configure(text=result)
    
    def quit_game(self):
        self.window.withdraw()        