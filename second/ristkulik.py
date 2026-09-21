import math


a = float(input("Sisesta külg a: "))
b = float(input("Sisesta külg b: "))

pindala = a * b
ümbermoot = 2 * (a + b)
diagonaal = math.sqrt(a**2 + b**2)

print(f"Ristküliku pindala: {pindala}")
print(f"Ristküliku ümbermõõt: {ümbermoot}")
print(f"Ristküliku diagonaal: {diagonaal}")