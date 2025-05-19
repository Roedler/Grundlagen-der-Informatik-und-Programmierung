print("Umrechnung von Temperaturskalen (°C, °F, K)")
print("Auswahl des einzugebenden Temperaturskala (1: °C, 2: °F, 3: K)")
skala = input("Bitte wählen Sie die Temperaturskala (1/2/3): ")
wert = float	(
		 input("Temperaturwert: "))

if skala
== "1":
#Celsius
	grad_c = wert
		grad_f = grad_c * 9 / 5 + 32
		k = grad_c + 273.15
		print(f "\n{grad_c:.2f} °C entsprechen {grad_f:.2f} °F und {k:.2f} K.")

elif skala == "2":
#Fahrenheit
	grad_f = wert
		grad_c = (grad_f - 32) * 5 / 9
		k = (grad_f - 32) / 1.8 + 273.15
		print(f "\n{grad_f:.2f} °F entsprechen {grad_c:.2f} °C und {k:.2f} K.")

elif skala == "3":
#Kelvin
	k = wert
		grad_c = k - 273.15
		grad_f = (k - 273.15) * 1.8 + 32
		print(f "\n{k:.2f} K entsprechen {grad_c:.2f} °C und {grad_f:.2f} °F.")

		else
:
	print("Ungültige Auswahl. Bitte wählen Sie 1, 2 oder 3.")

		print("\n(Die Berechnung wurde durchgeführt von Lennart Novak.)")
