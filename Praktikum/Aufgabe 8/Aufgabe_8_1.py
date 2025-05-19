einkaufsliste = []

while True:
    print("\nEinkaufslisten-Verwaltung:")
    print("==========================")
    print("Liste   (a)nzeigen")
    print("Liste   (e)rgänzen")
    print("Eintrag (l)öschen")
    print("Liste   l(ö)schen (alle Einträge!)")
    print("(P)rogrammende")
    auswahl = input("Auswahl: ").strip().lower()

    if auswahl == "a":
        if einkaufsliste:
            print("\nAktuelle Liste:")
            for id, item in enumerate(einkaufsliste, 1):
                print(f"{id}. {item}")
        else:
            print("\nDie Einkaufsliste ist leer.")

    elif auswahl == "e":
        print("\nNeuer Listeneintrag (Abbruch mit Enter):")
        while True:
            eintrag = input("Eintrag: ").strip()
            if not eintrag:
                break
            einkaufsliste.append(eintrag)
        print("\nAktuelle Liste:")
        for id, item in enumerate(einkaufsliste, 1):
            print(f"{id}. {item}")

    elif auswahl == "l":
        print("\nZu löschender Listeneintrag (Abbruch mit Enter):")
        while True:
            eintrag = input("Eintrag: ").strip()
            if not eintrag:
                break
            if eintrag in einkaufsliste:
                einkaufsliste.remove(eintrag)
                print(f"{eintrag} wurde aus der Liste entfernt.")
            else:
                print(f"{eintrag} ist nicht in der Liste.")
        print("\nAktuelle Liste:")
        for id, item in enumerate(einkaufsliste, 1):
            print(f"{id}. {item}")

    elif auswahl == "ö":
        einkaufsliste.clear()
        print("\nDie Einkaufsliste wurde geleert.")

    elif auswahl == "p":
        print("\nProgrammende!")
        print("Das Programm wurde ausgeführt von Lennart Novak.")
        break

    else:
        print("\nUngültige Auswahl, bitte erneut versuchen.")
