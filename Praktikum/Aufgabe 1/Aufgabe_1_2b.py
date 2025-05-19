vorname = input('Vorname: ')
nachname = input('Nachname: ')
strasse = input('Strasse: ')
hausnummer = int(input('Hausnummer: ')) #Gibt es bezüglich der Eingabe der Hausnummer Besonderheiten?
# Ja die Hausnummer muss bei der Eingabe als Integer deklariert worden sein.
PLZ = input('PLZ: ')
ort = input('Ort: ')

print(f"\n{vorname} {nachname}")
print(f"{strasse} {hausnummer}")
print(f"{PLZ} {ort}")
