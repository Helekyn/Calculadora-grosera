print("Hola soy calculín y puedo: sumar(+), restar(-), dividir(/) y multiplicar(*)...")

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

    aritmetica = str(input("¿Que operación quieres(+),(-),(*),(/):?"))

    if aritmetica == "+":
        print(num1 + num2)
    elif aritmetica == "-":
        print(num1 - num2)
    elif aritmetica == "/":
        if num2 == 0:
            print("ERROR: No se puede dividir x 0 me da ansiedad.")
        else:
            print(num1 / num2)
    elif aritmetica == "*":
        print(num1 * num2)
    else:
        print("Error, sigue las instrucciones soy medio pelotudo")
        break

    salir_volver = input("Escribe ´S´ para continuar o ´N´ para salir:").upper()

    if salir_volver == "N":
        break
    elif salir_volver == "S":
        continue

print("Adiós amigo te extrañaré...")
