centimeters = float(input("CM: "))
inches = 0.3937 * centimeters
feat = 0.03281 * inches

print(f"Eine Länge von: \t{centimeters:.3f} cm")
print(f"entspricht: \t\t{inches:.3f} in")
print(f"bzw.: \t\t\t\t{feat:.3f} ft")
print(f"\nDie Berechnung wurde durchgeführt von: Lennart Novak.")
