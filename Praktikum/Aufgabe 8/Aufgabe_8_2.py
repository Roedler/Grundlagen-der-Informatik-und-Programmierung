while True:
    print("\nSatzanalyse:")
    eingabe = input("Eingabe (Abbruch mit <Enter>): ")

    if not eingabe:
        print("\nDie Zeichenanalyse wurde durchgeführt von Lennart Novak.")
        break

    eingabe_liste = list(eingabe.upper())

    eingegebene_vokale = []
    eingegebene_konsonanten = []
    eingegebene_leerzeichen = []
    eingegebene_satzzeichen = []
    eingegebene_ziffern = []

    vokale = "AEIOUÄÖÜ"
    konsonanten = "BCDFGHJKLMNPQRSTVWXYZ"
    satzzeichen = ".,!?;:"
    ziffern = "0123456789"

    for zeichen in eingabe_liste:
        if zeichen in vokale:
            eingegebene_vokale.append(zeichen)
        elif zeichen in konsonanten:
            eingegebene_konsonanten.append(zeichen)
        elif zeichen == " ":
            eingegebene_leerzeichen.append(zeichen)
        elif zeichen in satzzeichen:
            eingegebene_satzzeichen.append(zeichen)
        elif zeichen in ziffern:
            eingegebene_ziffern.append(zeichen)

    print(f"\nDer eingegebene Text enthält {len(eingegebene_vokale)} Vokale, {len(eingegebene_konsonanten)} Konsonanten, {len(eingegebene_leerzeichen)} Leerzeichen, {len(eingegebene_satzzeichen)} Satzzeichen und {len(eingegebene_ziffern)} Ziffern.")
    print("In sortierter Ausgabe ergeben sich folgende Listen:")
    print(f"Vokale:      {sorted(eingegebene_vokale)}")
    print(f"Konsonanten: {sorted(eingegebene_konsonanten)}")
    print(f"Satzzeichen: {sorted(eingegebene_satzzeichen)}")
    print(f"Ziffern:     {sorted(eingegebene_ziffern)}")
