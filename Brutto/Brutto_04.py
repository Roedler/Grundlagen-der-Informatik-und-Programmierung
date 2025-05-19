# Berechnung des Bruttopreises
strNettopreis = input("Nettopreis: ")
fltNettopreis = float(strNettopreis)
fltBruttopreis = 1.19 * fltNettopreis
print("Bruttopreis:", format(fltBruttopreis, '8.2f'))
print("Für einen Nettopreis von", format(fltNettopreis, '8.2f'), "€ ergibt sich ein Bruttopreis von", format(fltNettopreis, '8.2f'))
