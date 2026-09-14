 # Loo skript mis küsib kasutajalt ringi raadiust ja
 # arvutab ringi pindala ning ümbermõõdu. 
 # Kasutaja sisestab raadiuse, seejärel
 # Kontrolli kas raadius on vahemikus 1-10. Kui pole õiges vahemikus
 # Ütle, et raadius on vales vahemikus
 # skript kuvab tulemused.

from math import pi
radius = float(input("Sisesta ringi raadius: "))
if radius < 1 or radius > 10:
    print("Raadius on vales vahemikus")
def ring_area(radius):
    return pi * radius ** 2
def ring_circumference(radius):
    return 2 * pi * radius

if 1 <= radius <= 10:
    print(f"Ringi pindala: {ring_area(radius)}")
    print(f"Ringi ümbermõõt: {ring_circumference(radius)}")