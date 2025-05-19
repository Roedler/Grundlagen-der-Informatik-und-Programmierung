P_x = float(input("Geben Sie die x-Koordinate des Punktes ein: "))
P_y = float(input("Geben Sie die y-Koordinate des Punktes ein: "))

if P_x > 0 and P_y > 0:
    quadrant = "im 1. Quadrant"
elif P_x < 0 and P_y > 0:
    quadrant = "im 2. Quadrant"
elif P_x < 0 and P_y < 0:
    quadrant = "im 3. Quadrant"
elif P_x > 0 and P_y < 0:
    quadrant = "im 4. Quadrant"
elif P_x == 0 and P_y != 0:
    quadrant = "auf der y-Achse"
elif P_y == 0 and P_x != 0:
    quadrant = "auf der x-Achse"
else:
    quadrant = "im Ursprung"

print(f"\nDer Punkt P mit den Koordinaten:")
print(f"x = {P_x:.2f}")
print(f"y = {P_y:.2f}")
print(f"liegt {quadrant}.")
