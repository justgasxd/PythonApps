# Listid
# List ehk massiiv
# List [nimekiri, loend], tuple (järjend), dictionary {sõnastik}

places = [] #Loo tühi list
places.append('Kehtna') # Lisa uus koht listi lõppu
places.append('Rapla')
places[1:1] = ['Tallinn', 'Pärnu'] # Lisa Kehtna ka Rapla vahele
places.extend(['Viljandi', 'Tartu', 'Rapla']) # Lisa lõppu
places.insert(2, 'Are')

numbers = [1, 7, 75, 3 ,-534]

print(places) # Näita kohanimede listi
print(numbers) # Näita numbrite listi
print(type(places)) # Näita kohanimede muutuja tüüpi

# Kustutamine
places.remove('Rapla') # Esimene eemaldatakse
places.pop(6) # Viimane Rapla kustutatakse
del places[2] # Kustutab Are

# Ülesanne: Lisa Rapla, Pärnu ja Viljandi vahele ning listi lõppu
places[2:3] = ['Pärnu', 'Rapla']
places.extend(['Rapla'])
print (places)

# Leiame elemendi indeksi ja mitu korda esineb ()
place = places[-1] # Nimekirja viimane Rapla
index = places.index(place) # Mis indeks on esiemene Rapla
count = places.count(place) # Mitu Raplat leiti

print(place, index, count)

if place in places:
    print(f'{place} on nimekirjas olemas.')

if 'Kohila' in places:
    print(f'Kohila on nimekirjas olemas.') # Seda rida vastusesse ei tule
    
print(len(places))    # Listi suurus
print(places[len(places)-1]) # Viimane element listist

# Koopia listist
list_copy = places.copy()
list_list = list(places)

# Sorteerimine
list_copy.sort() # A-Z
new_list_list = sorted(places, reverse=True)

print(list_copy) #sorteeritud
print(new_list_list) # Z-A
print(places) # Originaal

print() # Tühi rida

# Tühjenda list
new_list_list.clear()
print(new_list_list)

"""
Ülesanne: kasuta originaal listi ja eemalda listist viimane Rapla
ilma [-1] kasutamata. Väljasta kolmanda elemendi keskmine täht suuretähena
"""
del places [6]
print(places) # Kontrolli eelmise rea tulemusi
print(places[2][2].title()) # Pärnu => R
