# gui.py
import csv
from datetime import datetime
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, simpledialog, ttk

from game import GuessGame

SCORES_FILE = Path(__file__).with_name('scores.csv')

class GuessGameApp:
    def __init__(self, root):

        self.root = root
        self.root.title('Arva ära number (1-100)')
        self.root.geometry('480x470')
        self.root.resizable(False, False)
        # TODO Loo mäng
        self.game = GuessGame()
        print(self.game.secret_number)

        main = ttk.Frame(root, padding=20)
        main.pack(fill='both', expand=True)

        ttk.Label(main, text='Arva ära', font=('Arial', 18, 'bold')).pack(pady=(0,0))
        ttk.Label(main, text='Arvuti valis arvu vahemikus 1-100').pack()

        self.entry = ttk.Entry(main, font=('Arial', 14), justify='center', width=15)
        self.entry.pack(pady=12)
        self.entry.focus_set()
        # TODO Enter klahviga saab sisestada
        self.entry.bind('<Return>', self.check_guess)

        buttons = ttk.Frame(main)
        buttons.pack()
        ttk.Button(buttons, text='Kontrolli', command= self.check_guess).pack(side='left', padx=5)
        ttk.Button(buttons, text='Uus mäng', command=self.new_game).pack(side='left', padx=5)
        ttk.Button(buttons, text='Edetabel', command=self.show_scores).pack(side='left', padx=5)

        self.message_label = ttk.Label(main, text='Sisesta oma esimene pakkumine', font=('Arial', 11))
        self.message_label.pack(pady=(14, 10))

        ttk.Label(main, text='EELMISED PAKKUMISED', font=('Arial', 11, 'bold')).pack()
        history_frame = ttk.Frame(main)
        history_frame.pack(fill='both', expand= True, pady=(6, 10))

        self.history = tk.Text(history_frame, height=10, width=44, state='disabled', font=('Consolas', 11))
        self.history.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(history_frame, orient='vertical', command=self.history.yview)
        scrollbar.pack(side='right', fill='y')
        self.history.configure(yscrollcommand=scrollbar.set)

        self.attempts_label = ttk.Label(main, text='', font=('Arial', 11, 'bold'))
        self.attempts_label.pack(pady=(2, 4))
       
        self.center_window()



    def center_window(self):
        """Paigutab mängu akna ekraani keskele"""
        self.root.update_idletasks()

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        screen_width =self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f'+{x}+{y}')


    def add_history(self, number, result):
        self.history.config(state='normal')
        self.history.insert(tk.END, f'{number:>3} - {result}\n')
        self.history.see(tk.END)
        self.history.config(state='disabled')


    def check_guess(self, event=None):
        value = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if self.game.finished:
            self.message_label.config(text='Alustamiseks vajuta "Uus mäng"')
            return

        if value.lower() == 'backdoor':
            number = self.game.reveal_number()
            self.message_label.config(text=f'Salajane arv on {number}. (Petukood kasutatud)')
            self.entry.focus_set()
            return

        try:
            number = int(value)
        except ValueError:
            messagebox.showwarning('Vale sisestus', 'Sisesta täisarv vaemikus 1-100')
            self.entry.focus_set()
            return

        if not 1 <= number <= 100:
            messagebox.showwarning('Vale sisestus', 'Arv peab olema vahemikus 1-100')
            self.entry.focus_set()
            return

        result = self.game.guess(number)
        self.message_label.config(text=result)
        self.add_history(number, result)

        if self.game.finished:
            self.attempts_label.config(text=f'Arvasid ära {self.game.attempts} katsega!')
            if self.game.cheated:
                messagebox.showinfo('Mäng läbi', 'Petukoodi kasutamise töttu tulemust ei salvestata')
            else:
                name = simpledialog.askstring('Võit', 'Õige vastus! Sisesta oma nimi:', parent=self.root)


                if name and name.strip():
                    self.save_score(name.strip()[:30], self.game.attempts)
        self.entry.focus_set()

    def save_score(self, name, attempts):
        scores = self.read_scores()
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        scores.append((name, attempts, date_time ))
        scores.sort(key=lambda item: item[1])
        with open(SCORES_FILE, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(scores[:10])

    def new_game(self):
        self.game.new_game()
        self.entry.delete(0, tk.END)
        self.message_label.config(text='Uus mäng! Sisesta oma pakkumine')
        self.attempts_label.config(text='')
        self.history.config(state='normal')
        self.history.delete('1.0', tk.END)
        self.history.config(state='disabled')
        self.entry.focus_set()

    def read_scores(self):
        scores = []
        if SCORES_FILE.exists():
            with open(SCORES_FILE, 'r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    if len(row) < 2:
                        continue
                    try:
                        attempts = int(row[1])
                    except ValueError:
                        continue
                    if attempts > 0:
                        # Varasemates failides oli ainult nimi ja katsete arv
                        date_time = row[2] if len(row) >= 3 else ''
                        scores.append((row[0], attempts, datetime))
        return sorted(scores, key=lambda item: item[1])[:10]


    def show_scores(self):
        window = tk.Toplevel(self.root)
        window.title('Edetabel - TOP 10')
        window.geometry('580x330')
        window.resizable(False, False)
        window.transient(self.root)
        window.grab_set()

        ttk.Label(window, text='Edetabel - TOP 10', font=('Arial', 14, 'bold'))
        score_list = tk.Listbox(window, width=68, height=15, font=('Consolas', 10))
        score_list.pack(padx=15, pady=5)

        scores = self.read_scores()
        if not scores:
            score_list.insert(tk.END, 'Edetabel on veel tühi.')
        for position, (name, attempts, date_time) in enumerate(scores, start=1):
            score_list.insert(tk.END, f'{position:>2}. {name:>20} {attempts:>3} katset {date_time}')

        ttk.Button(window, text='Sulge', command=window.destroy).pack(pady=10)