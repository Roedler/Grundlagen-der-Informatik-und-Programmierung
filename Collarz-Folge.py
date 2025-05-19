while True:
    z = int(input("n = "))
    i = 1

    if z == 0:
        break

    while z != 1:
        if z % 2 == 0:
            z = z / 2
        else:
            z = z * 3 + 1

        print(f"{i:10d}. Durchlauf: z = {z}")
        i += 1
