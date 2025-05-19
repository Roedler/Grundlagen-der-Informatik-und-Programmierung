def berechne_bakterienwachstum(stunden):
    anzahl_bakterien = [1]
    for stunde in range(1, stunden + 1):
        anzahl_bakterien.append(anzahl_bakterien[-1] * 8)
    return anzahl_bakterien

def berechne_gesamtgewicht(bakterien_liste):
    letzte_anzahl = bakterien_liste[-1]
    gewicht_pro_bakterium = 1.1e-12
    gesamtgewicht = letzte_anzahl * gewicht_pro_bakterium
    return gesamtgewicht

while True:
    stunden = int(input("Anzahl der Stunden (0 zum Beenden): "))
    if stunden == 0:
        break

    bakterien_entwicklung = berechne_bakterienwachstum(stunden)
    gesamtgewicht = berechne_gesamtgewicht(bakterien_entwicklung)

    print("Entwicklung der Bakterienanzahl:")
    for stunde, anzahl in enumerate(bakterien_entwicklung):
        if anzahl == 1:
            print(f"Stunde {stunde}: {anzahl:,} Bakterieg")
        else:
            print(f"Stunde {stunde}: {anzahl:,} Bakterien")

    print(f"Gesamtgewicht nach {stunden - 1} Stunden: {gesamtgewicht:.12f} g")