nachname = "Novak"
vorname = "Lennart"
strasse = "Teststraße"
hausnummer = 23
PLZ = "47051" # ist hier nicht besser integer zu verwenden? Warum?
# Weil Postleitzahlen auch mit einer 0 beginnen können und ein Integer kann nicht mit einer 0 beginnen.
ort = "Duisburg"

print(vorname,nachname)
print(strasse,hausnummer)
print(PLZ,ort)
