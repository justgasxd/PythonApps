# game.py
import random

class GuessGame:
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.finished = False
        self.cheated = False

    def guess(self, number):
        if self.finished:
            return 'Mäng on juba lõppenud'

        self.attempts += 1

        if number < self.secret_number:
            return 'Liiga väike!'
        if number > self.secret_number:
            return 'Liiga suur!'

        self.finished = True
        return 'Õige vastus!'

    def reveal_number(self):
        self.cheated = True
        return self.secret_number