import math


def es_numero_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


def pedir_numero():
    while True:
        dato = input("Ingresa un numero entero: ")
        try:
            return int(dato)
        except ValueError:
            print("Eso no es un numero entero, proba de nuevo.")


if __name__ == "__main__":
    numero = pedir_numero()
    resultado = "es primo" if es_numero_primo(numero) else "no es primo"
    print(f"{numero} {resultado}")
