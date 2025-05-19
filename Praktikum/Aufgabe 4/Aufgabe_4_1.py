def bestimme_gefahr(schallpegel):
    if schallpegel < 40:
        return "vollkommen ungefährlich"
    elif 40 <= schallpegel <= 65:
        return "ungefährlich, aber Konzentrationsstörungen möglich"
    elif 65 < schallpegel <= 85:
        return "meist ungefährlich, aber erhöhtes Krankheitsrisiko"
    elif 85 < schallpegel <= 120:
        return "gefährlich bei längerer Einwirkung (40h/Woche), Hörschäden"
    else:
        return "sehr gefährlich, auch bei kurzer Einwirkung, Gehörschäden"

while True:
    schallpegel = int(input("Schallpegel (dB): "))
    if schallpegel == 0:
        print("Sie haben die Schallpegelabfrage beendet.")
        break

    gefahr = bestimme_gefahr(schallpegel)
    print(f"Für einen Schallpegel von {schallpegel} dB gilt:")
    print(gefahr)