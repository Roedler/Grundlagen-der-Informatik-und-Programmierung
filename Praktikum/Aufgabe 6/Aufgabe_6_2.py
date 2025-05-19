import turtle

def fktZeichneN_Eck(n, x, y, l, f):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(f)
    turtle.begin_fill()
    winkel = 360 / n
    for _ in range(n):
        turtle.forward(l)
        turtle.left(winkel)
    turtle.end_fill()

def fktStrecke(x_p, y_p, x_q, y_q, farbe):
    turtle.penup()
    turtle.goto(x_p, y_p)
    turtle.pendown()
    turtle.pencolor(farbe)
    turtle.goto(x_q, y_q)

turtle.penup()

while True:
    try:
        n = int(input("Anzahl der Ecken (0 zum Beenden, 2 um eine Linie zu malen): "))
        if n == 0:
            break
        x = float(input("x-Koordinate: "))
        y = float(input("y-Koordinate: "))

        if n == 2:
            x_q = float(input("x-Koordinate von Punkt Q: "))
            y_q = float(input("y-Koordinate von Punkt Q: "))
            farbe = input("Farbe der Strecke: ")
            fktStrecke(x, y, x_q, y_q, farbe)
        else:
            l = float(input("Seitenlänge: "))
            f = input("Füllfarbe: ")
            fktZeichneN_Eck(n, x, y, l, f)

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie numerische Werte ein.")

turtle.done()