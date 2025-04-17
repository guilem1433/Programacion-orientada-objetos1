numero1 = 645432
numero2 = 54

def mcd(numero1,numero2):
    while numero2:
        numero1, numero2 = numero2, numero1 % numero2
    return numero1
print(f"El mcd de {numero1} y {numero2} es {mcd(numero1,numero2)}")