 # read_csv_v2.py
"""
Täiendus: loenda kokku mitu numbrit kokku liidetakse
Näita ka vastust
"""
filename = 'Create-MyCSV-s.csv'
total = 0 # Kogu veeru summa
count = 0 # 1. Täiendus

# Loe kokku mitu veergu on failis
f = open(filename, 'r') # Ava fail lugemiseks
rows = len(f.readline().split(';')) # Mitu elementi reas
f.close() # Sulge fail

row = int(input(f'Mitmes veerg kokku liita? 1-{rows} '))

if row >= 1 and row <= rows:
    row -= 1 # Row = row -1

    with open(filename, 'r') as f:
        content = f.readlines()
        for line in content:
            line = line.strip() # Korrasta rida (eemaldab \n)
            parts = line.split(';') 
            if parts[row].isnumeric():
                total += int(parts[row])
                count += 1 # Kasva ühe võrra
        # print(line)
        print(total, count)

else:
    print('Vigane veeru number!')