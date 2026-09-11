import datetime # Kuupäevade arvutamiseks
# See on kommentaar

"""
mitme realine
kommentaar
"""

# Muutujate omistamine
name = 'reimo novošilov'
age = 16
height = 1.7 # Alati punkt!

print (name, age, height)
# Kasutaja NAME vanuses AGE on pikkusega HEIGHT meetrit
print(f'Kasutaja {name.title()} vanusega {age}a. on pikkusega {height} meetrit.')
print('Kasutaja ' + name.title() + ' vanusega '+ str(age) + 'a. on pikkusega '+ str(height) + ' meetrit.')

# Jooksev aasta
birth_year = datetime.date.today().year - age
print(f'Sünniaasta: {birth_year}')

age = int(input('Sisesta vanus: '))

if age < 1 or age > 122:
    print('Vanus on vales vahemikus (lubatud 1-122 k.a.)')
elif age < 18:
    print('Alaealine') #1-17
elif age < 64:
    print('Tööealine') #18-64
elif age < 100:
    print ('Pensionär') # 65-99
else:
    print('Pikaealine') # 100-122

"""
Küsime elukohta ja vastavalt elukoha nime pikkusele väljastame
Lühike nimi (2-6 tähte)
Pikk nimi (7- tähte)
"""

place =  input('Sisesta elukoht: ')
place = place.strip() # Eemaldab tühikud algusest ja lõpust

if len(place) > 1 and len(place) <= 6 and place.isalpha():
    print(f'Lühike nimi {place}')
elif len(place) > 6 and place.isalpha():
    print(f'Pikk nimi {place}')
else:
    print('Viga!')
    
    
# Substring (alamstringid)
# Muutuja name = 'reimo novošilov'
print(name)
print(name[1])   # Väljund: e
print(name[1:5]) # Väljund: eimo
print(name[6:])  # Väljund: novošilov
print(name[:5])  # Väljund: reimo
print(name[:: -1]) # Väljund volišovon omier

# Muutujast name väljastage perekonnanime esiemene täht SUURELT
print(name[6].title())


# Kolm andmetüüpi
print('-----')
print(type(name))
print(type(age))
print(type(height))
