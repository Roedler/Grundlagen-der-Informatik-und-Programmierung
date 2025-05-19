def calculate_string_code(input_string):
    total = 0
    for i, char in enumerate(input_string):
        ascii_value = ord(char)
        multiplier = 2 ** i
        total += ascii_value * multiplier
    return total

print("Zeichenketten-Codierung\n")
print("Eingabe einer Zeichenkette der Länge 6-12.\n")

valid_count = 0

while True:
    input_string = input("Zeichenkette (Abbruch mit 'A'): ")

    if input_string == "A":
        break

    if not (6 <= len(input_string) <= 12):
        print("Ungültige Länge! Die Zeichenkette muss zwischen 6 und 12 Zeichen lang sein.\n")
        continue

    code = calculate_string_code(input_string)
    print(f"Für die Zeichenkette \"{input_string}\" ergibt sich der Code: {code}.\n")

    valid_count += 1

print("Programmende. Das Programm wurde aufgerufen von Lennart Novak.")
print(f"Es wurden insgesamt {valid_count} gültige Kodierungen vorgenommen.")

