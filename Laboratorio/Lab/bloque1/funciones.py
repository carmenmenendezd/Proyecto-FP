from dataclasses import dataclass

def primo(numero:int):
    if numero <= 1:
        return False  # Los números negativos, 0 y 1 no son primos

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible por algún número en este rango, no es primo

    return True  # Si no se encontró ningún divisor, es primo

if primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
