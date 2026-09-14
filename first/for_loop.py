from random import randint

names = ["Mari", "Anna", "Villem", "Jüri"]

# Väljasta listis olevad nimed nime kaupa
for name in names:
    print(name) # Väljasta nimi

print() #tühi rida

#Sama lahendus nagu enne, aga lisaks juhuslik vanus
for x in range(len(names)):
    print(x, names[x], randint(1, 122))

print()

for x in range (1, 5): # 1 2 3 4
    print (x, end= ' ') # Ei tee reavahetust
print('\n') # Reavahetus + tühi rida

for x in range(0, 10, 2):
    print(x, end=' | ')
print ('\n') # Reavahetus + tühi rida

# while-loop
x = 0
while x < len(names):
    print(names[x])
    x += 1 # x = x + 1

# Ülesanne: Väljasta listi nimed konsooli ja pane iga nime ette järjekorranumber koos punktiga
#1. mari
#2. Anna
#....
for x in range(len(names)):
    print(f'{x+1}. {names[x]}')

    