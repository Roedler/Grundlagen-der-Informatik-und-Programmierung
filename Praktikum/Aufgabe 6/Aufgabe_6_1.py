import math

def fktVolumenEllipsoid(a=0, b=0, c=0):
    if a == 0 or b == 0 or c == 0:
        return 0
    return (4/3) * math.pi * a * b * c

def fktOberflaecheEllipsoid(a=0, b=0, c=0):
    if a == 0 or b == 0 or c == 0:
        return 0
    return 4 * math.pi * ((((a * b)**(8/5) + (a * c)**(8/5) + (b * c)**(8/5)) / 3)**(5/8))

def fktEllipsoid(a=0, b=0, c=0):
    if a == 0 or b == 0 or c == 0:
        return None
    volume = fktVolumenEllipsoid(a, b, c)
    if abs(a - b) / a < 0.001 and abs(a - c) / a < 0.001:
        surface = 4 * math.pi * (a**2)
        exact = True
    else:
        surface = fktOberflaecheEllipsoid(a, b, c)
        exact = False
    return volume, surface, exact

print("Calculation of the volume and (approximated) surface area of a triaxial ellipsoid:")
while True:
    try:
        a = float(input("Axis length a = "))
        if a == 0:
            break
        b = float(input("Axis length b = "))
        c = float(input("Axis length c = "))
        result = fktEllipsoid(a, b, c)
        if result is None:
            print("Invalid input. Axes cannot be 0.")
            continue
        volume, surface, exact = result
        print(f"\nFor an ellipsoid with axis lengths a= {a:.2f}, b= {b:.2f}, and c= {c:.2f}:")
        print(f"Volume   = {volume:.2f}")
        if exact:
            print(f"Surface  = {surface:.2f} (exact)")
        else:
            print(f"Surface  = {surface:.2f} (approximated)")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

print("\nCalculations completed.")
