# Game.py
"""
Ära arvamise mäng. Mõeldud numberid on 1-100.
Loetakse samme. Mängul on takauks (1000)
TÄIENDUS: Mängu lõppedes küsin kasutajalt kas soovib
veel mängida? Kui jah (J, j), sii sreseti andmed ja alusta uut mängu
1. Kuhu kirjutada mida, mida kirjutada, kas teha funktsioon?
"""
from random import randint

pc_nr = randint(1, 100) #Arvuti mõeldud number
steps = 0 # Sammude lugeja
game_over = False # Kas mäng on läbi?

#print(pc_nr) #TEST!

def ask():
    global steps, game_over # Globaalsed muutujad
    user_nr = int(input('Sisesta number: '))
    steps += 1 # Sammud kasvavad +1

    if user_nr > pc_nr and user_nr != 1000:
        print('Väiksem')
    elif user_nr < pc_nr and user_nr != 1000:
        print('Suurem')
    elif user_nr == pc_nr and user_nr != 1000: 
        game_over = True
        print(f'Arvasid numbri ära {steps} sammuga')
    elif user_nr == 1000:
        print(f'Leidsid mu nõrga koha. Number on {pc_nr}')

def lets_play():
    while not game_over:
        ask()
    play_again()

def play_again():
    global pc_nr, steps, game_over
    result = input('Kas mängime veel? [J/E] ')
    if result == 'J' or result == 'j':
        pc_nr = randint(1, 100)
        steps = 0
        game_over = False
        lets_play()
lets_play()