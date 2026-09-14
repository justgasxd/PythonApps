 # read_csv_v1.py

filename = 'Create-MyCSV-v.csv'
row = 2 # Mitmes veerg kokku liita
total = 0 # Kogu veeru summa

f = open(filename, 'r') # Ava fail lugemiseks
content = f.readlines() 
f.close() # Sulge fail

for line in content:
    line = line.strip() # Korrasta rida (eemaldab \n)
    parts = line.split(';') 
    if parts[row].isnumeric():
        total += int(parts[row])
        # print(line)

    # print(parts)
print(total)