# create_file.py

from random import randint

name = input('Sisesta nimi: ')

with open('create_file.txt', 'a', encoding='utf-8') as f:
    f.write(f"{name} ; {randint(1, 122)}\n")