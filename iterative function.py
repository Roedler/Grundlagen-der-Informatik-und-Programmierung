def calcFakultaet(n):
    erg = 1
    while n > 1:
        erg = erg * n
        n -= 1
    return erg

print(calcFakultaet(10))