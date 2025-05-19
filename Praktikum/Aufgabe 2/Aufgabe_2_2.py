name = input("Ihr Vorname: ")
a = float(input("Kantenlänge der quadratischen Grundseite (in m): "))
h = float(input("Höhe der Säule (in m): "))

surfaceArea = 2 * a**2 + 4 * a * h
volume = a**2 * h
spaceDiagonal = (2 * a**2 + h**2)**0.5

print(f"\nDie von {name} berechnete quadratische Säule mit der")
print(f"Grundkantenlänge {a:,.2f} m und der Höhe {h:,.2f} m")
print(f"besitzt ein Volumen von {volume:,.2f} m³")
print(f"und eine Oberfläche von {surfaceArea:,.2f} m².")
print(f"Die Länge der Raumdiagonalen beträgt {spaceDiagonal:,.2f} m.")
