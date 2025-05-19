def fktA(n):
    if n == 1:
        return 1
    else:
        return 1 - (1 / (1 + fktA(n - 1)))

def fktB(a, n):
    if n == 1:
        return a
    else:
        return a * fktB(a, n - 1)

while True:
    print("Berechnung der rekursiven Funktionen im Intervall [n_min, n_max] (Abbruch mit 0):")
    try:
        n_min = int(input("n_min = "))
        if n_min == 0:
            break
        n_max = int(input("n_max = "))
        a = float(input("a = "))
    except ValueError:
        print("Bitte geben Sie gültige Zahlen ein.")
        continue

    print(f"\nFür a={a:.2f} ergeben sich im Intervall [{n_min}, {n_max}] folgende Werte:\n")

    # Kopfzeile der Tabelle
    header = f"{'n':>4}{'fktA(n)':>12}{'fktB(a,n)':>12}{'fktA(n) * fktB(a,n)':>22}"
    print(header)
    print("-" * len(header))

    for n in range(n_min, n_max + 1):
        fa = fktA(n)
        fb = fktB(a, n)
        product = fa * fb

        # Begrenzen der Nachkommastellen und der Spaltenbreiten
        print(f"{n:4}{fa:12.2f}{fb:12.2f}{product:20.2f}")

    print("\n")

print("Ende der Programmausführung. Die Berechnung wurde durchgeführt von Lennart Novak.")
