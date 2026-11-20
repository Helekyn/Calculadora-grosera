print("Hola soy calculín y puedo: sumar(+), restar(-), dividir(/) y multiplicar(*)")


def adicion(num1, num2):
    return num1 + num2


def sustraccion(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


while True:
    try:
        num1 = float(input("Bien, dame un número:"))
    except ValueError:
        print("Dije nú-me-ro.")
        continue

    try:
        num2 = float(input("Ahora el otro:"))
    except ValueError:
        print("Dije nú-me-ro.")
        continue

    aritmetica = input("¿Que operación quieres(+),(-),(*),(/):?")

    if aritmetica == "+":
        print(adicion(num1, num2))

    elif aritmetica == "-":
        print(sustraccion(num1, num2))

    elif aritmetica == "/":
        if num2 == 0:
            print("ERROR: No se puede dividir por CERO, me causa ansiedad.")
        else:
            print(division(num1, num2))

    elif aritmetica == "*":
        print(multiplicacion(num1, num2))

    else:
        print("ERROR: Sigue las instrucciones de operación.")
        continue

    salir_volver = input("Escribe ´S´ para continuar o ´N´ para salir:").upper()

    if salir_volver == "N":
        print("Adiós, te extrañaré...")
        break
    elif salir_volver == "S":
        pass
    else:
        print("Llámame cuando aprendas a seguir instrucciones.")
        break
