import math


def raices_cuadratica(a, b, c):
    if a == 0:
        raise ValueError("El coeficiente a no puede ser 0")

    delta = b * b - 4 * a * c

    if delta < 0:
        return ()
    if delta == 0:
        return (-b / (2 * a),)

    raiz_delta = math.sqrt(delta)
    return ((-b + raiz_delta) / (2 * a), (-b - raiz_delta) / (2 * a))


def leer_coeficiente(nombre):
    while True:
        try:
            return float(input(f"Valor de {nombre}: "))
        except ValueError:
            print("Tiene que ser un numero.")


if __name__ == "__main__":
    a = leer_coeficiente("a")
    b = leer_coeficiente("b")
    c = leer_coeficiente("c")

    try:
        raices = raices_cuadratica(a, b, c)
    except ValueError as error:
        print(error)
    else:
        if len(raices) == 0:
            print("La ecuacion no tiene raices reales")
        elif len(raices) == 1:
            print(f"Tiene una sola raiz: {raices[0]}")
        else:
            print(f"Raices: {raices[0]} y {raices[1]}")
