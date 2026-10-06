# gui.py
import tkinter as tk
from tkinter import messagebox

from calculations import calculate_average, calculate_work_time, convert_temperature

def start_gui():
    global root, content

    root = tk.Tk()
    root.title('Abivahendid')
    root.geometry('430x330')
    root.resizable(False, False)

    create_menu()
    
    content = tk.Frame(root, padx=25, pady=25, bg='grey')
    content.pack(fill='both', expand=True,)

    show_home()

    root.mainloop()

def create_menu():
    menu = tk.Menu(root)
    root.config(menu=menu)

    tools_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='Tööriistad', menu=tools_menu)
    tools_menu.add_command(label='Hinnete keskmine', command=show_grades)
    tools_menu.add_command(label='Tööaja arvutamine', command=show_work_time)
    tools_menu.add_command(label='Temperatuuri teisendamine', command=show_temperature)

    program_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label='Programm', menu=program_menu)
    program_menu.add_command(label='Avaleht', command=show_home)
    program_menu.add_separator()
    program_menu.add_command(label='Välju', command=root.destroy)

def clear_home():
    """Eemaldab põhivormilt eelmise tööriista elemedid"""
    for widget in content.winfo_children():
        widget.destroy()

def show_home():
    clear_home()
    
    tk.Label(content, text='ABIVAHENDID',
            font=('Arial', 18, 'bold')).pack(
                pady=(35, 15))

    tk.Label(
    content,
    text='Vali menüüst Tööristad sobiv tööriist.',
    font=('Arial', 11)).pack()

def show_grades():
    clear_home()

    tk.Label(content, text='HINNETE KESKMINE',
            font=('Arial', 15, 'bold')).grid(
                row=0, column=0, columnspan=2, sticky='e',padx=5,pady=5)
    
    tk.Label(content, text='Hinne 1:').grid(
        row=1, column=0, sticky='e', padx=5, pady=5)
    grade1 = tk.Entry(content, width=12)
    grade1.grid(row=1, column=1, sticky='w', pady=5)
    grade1.focus_set() # Aktiivne lahter

    tk.Label(content, text='Hinne 2:').grid(
        row=2, column=0, sticky='e', padx=5, pady=5)
    grade2 = tk.Entry(content, width=12)
    grade2.grid(row=2, column=1, sticky='w', pady=5)

    tk.Label(content, text='Hinne 3:').grid(
        row=3, column=0, sticky='e', padx=5, pady=5)
    grade3 = tk.Entry(content, width=12)
    grade3.grid(row=3, column=1, sticky='w', pady=5)

    result_label = tk.Label(content, text='Keskmine hinne: -',
                            font=('Arial', 11, 'bold'))
    result_label.grid(row=5, column=0, columnspan=2, pady=15)

    def calculate():
        try:
            grades = [
                int(grade1.get()),
                int(grade2.get()),
                int(grade3.get())]
            if any(grade < 1 or grade > 5 for grade in grades):
                messagebox.showwarning('Vigane hinne', 'Hinne peab olema vahemikus 1-5 k.a.')
                return
            average = calculate_average(grades[0], grades[1], grades[2])
            result_label.config(text=f'Keskmine hinne: {average:.2f}')
        except ValueError:
            messagebox.showwarning('Vigane sisend', 'Sisesta kõik hinded täisarvuna')
    
    tk.Button(content, text='Arvuta', width=15, command=calculate).grid(row=4, column=0, columnspan=2, pady=10)

def show_work_time():
    clear_home()
    tk.Label(content,text='TÖÖAJA ARVUTAMINE',
             font=('Arial', 15, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    tk.Label(content, text='Töö algus: ').grid(row=1, column=0, sticky='w', pady=5)

    start_entry = tk.Entry(content, width=12)
    start_entry.grid(row=1, column=1, sticky='w', pady=5)
    start_entry.focus_set() # Aktiivne lahter
    tk.Label(content, text='Töö lõpp ').grid(row=2, column=0, sticky= 'w', pady=5)

    end_entry = tk.Entry(content, width=12)
    end_entry.grid(row=2, column=1, sticky='w', pady=5)

    tk.Label(content, text='Kasuta vormingut HH:MM').grid(row=3, column=0, columnspan=2, pady=(0,5))

    result_label = tk.Label(content, text='Töötatud aeg: -', font=('Arial', 11, 'bold'))
    result_label.grid(row=5, column=0, columnspan=2, pady=15)

    def calculate():
        try:
            hours, minutes = calculate_work_time(start_entry.get(), end_entry.get())
            result_label.config(text=f'Töötatud aeg: {hours} tundi {minutes} minutit')
        except ValueError:
            messagebox.showwarning('Vigane kellaaeg', 'Sisesta kellaaeg kujul HH:MM, näiteks 07:54')

    tk.Button(content, text='Arvuta', width=15, command=calculate).grid(row=4,column=0,columnspan=2,pady=10)

def show_temperature():
    clear_home()

    tk.Label(content, text='Teperatuuri teisendamine'.upper(), font=('Arial', 15,'bold')).grid(row=0, columnspan=2, pady=(0, 20))

    tk.Label(content, text='Temperatuur: ').grid(row=1,column=0,sticky='e',padx=5,pady=5)
    entry = tk.Entry(content, width=12)
    entry.grid(row=1, column=1, sticky='w', pady=5,)
    entry.focus_set()

    direction= tk.StringVar(value='C_TO_F')
    direction= tk.StringVar(value='F_TO_C')

    tk.Radiobutton(content, text='Celsius -> Fahrenheit',variable=direction, value='C_TO_F').grid(row=3, column=0, columnspan=2, sticky='w', padx=75)
    tk.Radiobutton(content, text='Fahrenheit -> Celsius',variable=direction, value='F_TO_C').grid(row=4, column=0, columnspan=2, sticky='w', padx=75)

    result = tk.Label(content, text='Tulemus: -', font=('Arial', 11, 'bold'))
    result.grid(row=5, column=0,columnspan=2, pady=15)

    def convert():
        try:
            temperature = float(entry.get().replace(',','.'))
            res = convert_temperature(temperature, direction.get())
            if direction.get() == 'C_TO_F':
                unit = 'F'
            else:
                unit = 'C'
            result.config(text=f'Tulemus: {res:.1f} {unit}')
        except ValueError:
            messagebox.showwarning('Vigane sisend', 'Sisesta temperatuur arvuna.')

    tk.Button(content, text='Teisenda', width=15, command=convert).grid(row=6, column=0, columnspan=2,pady=10)

