# Read_file.py
"""
Täiendus: Näita ainult neid isikuid kes on 100 ja rohkem vanad.
Täiendus2: Näita nendele isikutele sünniaastat (kasuta: datetime)
"""
from datetime import date # Täiendus 2
filename = "create_file.txt"

with open('create_file.txt', "r", encoding="utf-8") as f:
    contents = f.readlines() # Loe kõik read listi
    for line in contents:
        line = line.strip() # Korrasta rida
        name = line.split(';')[0] # Nimi
        age = int(line.split(';')[1]) # Teeb vanuse täisarvuks, muidu string
        if age >= 100:
            birth_year = date.today().year - age # Täiendus 2
        print(name ,age, birth_year)
        # print(type(name), type(age)) # näita nime ja vanuse tüüp
