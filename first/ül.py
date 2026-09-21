# Ülesanne 6

arv = int(input("Sisesta positiivne täisarv: "))
summa = 0
for i in range(1, arv + 1):
    summa = summa + i
print(f"Arvude summa alates 1-st kuni {arv} on {summa}.")