# gui.py
import csv
from datetime import datetime
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, simpledialog, ttk
import random

from game import GuessGame

SCORES_FILE = Path(__file__).with_name('scores.csv')

class GuessGameApp:
    def __init__(self, root):

        self.root = root
        self.root.title('Numbrite äraarvamise mäng')
        self.root.geometry('520x500')
        self.root.resizable(False, False)
        # TODO Loo mäng
        self.game = GuessGame()
       # print(self.game.secret_number)

        main = ttk.Frame(root, padding=20)
        main.pack(fill='both', expand=True)

        ttk.Label(
            main, text='Arva ära',
            font=('Arial', 18, 'bold')
        ).pack()

        self.range_label = ttk.Label(
            main, text='Arvuti valis arvu vahemikus 1-100'
        )
        self.range_label.pack()

        ttk.Label(main, text='Raskusaste:').pack(pady=(5, 0))

        self.difficulty = ttk.Combobox(
            main,
            values=('Lihtne', 'Tavaline', 'Raske'),
            state='readonly',
            width=15
        )
        self.difficulty.set('Tavaline')
        self.difficulty.pack()

        self.difficulty.bind(
            '<<ComboboxSelected>>',
            self.change_difficulty
        )

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
        self.history.insert(tk.END, f'{self.game.attempts}. {number:>3} - {result}\n')
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
           

            if not 1 <= number <= self.game.max_number:
                messagebox.showwarning(
                    'Vale sisestus',
                    f'Arv peab olema vahemikus 1-{self.game.max_number}'
                )
                self.entry.focus_set()
                return

        result = self.game.guess(number)
        self.message_label.config(text=result)

        if 'Õige vastus!' in result:
            self.message_label.config(foreground='green')
        elif 'väike' in result.lower() or 'suur' in result.lower():
            self.message_label.config(foreground='red')
        else:
            self.message_label.config(foreground='black')
        self.add_history(number, result)
        self.update_difficulty_state()



        if self.game.finished:
            self.attempts_label.config(text=f'Arvasid ära {self.game.attempts} katsega!')
            if self.game.cheated:
                messagebox.showinfo('Mäng läbi', 'Petukoodi kasutamise töttu tulemust ei salvestata')
            else:
                name = simpledialog.askstring('Võit', 'Õige vastus! Sisesta oma nimi:', parent=self.root)


                if name and name.strip():
                    self.save_score(
                        name.strip()[:30],
                        self.game.attempts,
                        self.difficulty.get()
                )
        self.entry.focus_set()

   
    def save_score(self, name, attempts, difficulty):
        scores = self.read_scores()
        date_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        scores.append((name, attempts, date_time, difficulty))

        # Parim tulemus on väikseima katsete arvuga.
        scores.sort(key=lambda item: item[1])

        with open(SCORES_FILE, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Nimi', 'Katsed', 'Kuupäev', 'Raskusaste'])
            writer.writerows(scores)


    
    def new_game(self):
        if self.game.attempts > 0 and not self.game.finished:
            answer = messagebox.askyesno(
                'Uus mäng',
                'Kas soovid poolelioleva mängu katkestada?',
                parent=self.root
            )
            if not answer:
                return

        ranges = {
            'Lihtne': 50,
            'Tavaline': 100,
            'Raske': 500
        }

        max_number = ranges[self.difficulty.get()]
        self.game.new_game(max_number)

        self.range_label.config(
            text=f'Arvuti valis arvu vahemikus 1–{max_number}'
        )

        self.difficulty.config(state='readonly')
        self.entry.delete(0, tk.END)
        self.message_label.config(
            text='Uus mäng! Sisesta oma pakkumine',
            foreground='black'
        )
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

                    if attempts <= 0:
                        continue

                    date_time = row[2] if len(row) >= 3 else ''

                    # Vanadel kirjetel raskusaste puudub.
                    difficulty = row[3] if len(row) >= 4 and row[3] else 'Tavaline'

                    if difficulty not in ('Lihtne', 'Tavaline', 'Raske'):
                        difficulty = 'Tavaline'

                    scores.append((
                        row[0],
                        attempts,
                        date_time,
                        difficulty
                    ))
        return sorted(scores, key=lambda item: item[1])

    
    
    def show_scores(self):
        window = tk.Toplevel(self.root)
        window.title('Edetabel - TOP 10')
        window.geometry('650x370')
        window.resizable(False, False)
        window.transient(self.root)
        window.grab_set()

        ttk.Label(
            window,
            text='Edetabel - TOP 10',
            font=('Arial', 14, 'bold')
        ).pack(pady=(12, 5))

        selector_frame = ttk.Frame(window)
        selector_frame.pack(pady=5)

        ttk.Label(
            selector_frame,
            text='Raskusaste:'
        ).pack(side='left', padx=5)

        difficulty_box = ttk.Combobox(
            selector_frame,
            values=('Lihtne', 'Tavaline', 'Raske'),
            state='readonly',
            width=15
        )
        difficulty_box.set('Tavaline')
        difficulty_box.pack(side='left', padx=5)

        score_list = tk.Listbox(
            window,
            width=78,
            height=12,
            font=('Consolas', 10)
        )
        score_list.pack(padx=15, pady=8)

        def refresh_scores(event=None):
            score_list.delete(0, tk.END)

            selected = difficulty_box.get()
            scores = [
                score for score in self.read_scores()
                if score[3] == selected
            ][:10]

            if not scores:
                score_list.insert(
                    tk.END,
                    'Selle raskusastme tulemused puuduvad.'
                )
                return

            for position, (name, attempts, date_time, difficulty) in enumerate(
                scores, start=1
            ):
                score_list.insert(
                    tk.END,
                    f'{position:>2}. {name:<20.20} '
                    f'{attempts:>3} katset  {date_time}'
                )

        difficulty_box.bind(
            '<<ComboboxSelected>>',
            refresh_scores
        )
        refresh_scores()

        ttk.Button(
            window,
            text='Sulge',
            command=window.destroy
        ).pack(pady=5)

    


    def change_difficulty(self, event=None):
        if self.game.attempts > 0 or self.game.finished:
            return

        ranges = {
            'Lihtne': 50,
            'Tavaline': 100,
            'Raske': 500
        }

        max_number = ranges[self.difficulty.get()]
        self.game.max_number = max_number
        self.game.secret_number = random.randint(1, max_number)

        self.range_label.config(
            text=f'Arvuti valis arvu vahemikus 1-{max_number}'
        )


    def update_difficulty_state(self):
        if self.game.attempts > 0 or self.game.finished:
            self.difficulty.config(state='disabled')
        else:
            self.difficulty.config(state='readonly')