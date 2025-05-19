anz_ja = anz_nein = anz_enthaltung = 0
while True:
    eingabe = input('Abstimmung (J/N/E) (Abbruch mit A): ')
    if eingabe == 'A': break
    elif (eingabe == 'N') or (eingabe == 'n'): anz_nein += 1
    elif (eingabe == 'J') or (eingabe == 'j'): anz_ja += 1
    elif (eingabe == 'E') or (eingabe == 'e'): anz_enthaltung += 1
    else: break

print(f"Ergebnis: \n Ja-Stimmen: {anz_ja} \n Nein-Stimmen: {anz_nein} \n Enthaltungen: {anz_enthaltung}")
