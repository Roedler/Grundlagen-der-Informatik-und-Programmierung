def calcFakultaet(n):
    if n == 1:
        erg = 1
    else:
        erg = n*calcFakultaet(n-1)
    return erg

print(calcFakultaet(2))