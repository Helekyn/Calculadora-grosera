while True:
    print(
        "Soy una calculadora y puedo: sumar(+), restar(-), dividir(/) y multiplicar(*) dos números..."
    )
    num1 = float(input("Bien, dame un número:"))
    num2 = float(input("Ahora el otro:"))

    while True:
        aritmetica = str(input("¿Que operación quieres?:"))

        if aritmetica == "+":
            print(num1 + num2)

        elif aritmetica == "-":
            print(num1 - num2)

        elif aritmetica == "/":
            print(num1 / num2)

        elif aritmetica == "*":
            print(num1 * num2)

        else:
            print(
                "Por favor escribe uno de los signos indicados para continuar [(+), (-), (/) o (*)]."
            )
            break

    input("Presiona cualquier tecla para continuar.")
    break
