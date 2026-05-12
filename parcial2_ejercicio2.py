from random import randint

limite_inferior = int(input("Ingrese limite inferior: "))
limite_superior = int(input("Ingrese limite superior: "))

if limite_inferior >= limite_superior:
    print("El limite inferior debe ser menor que el limite superior.")
else:
    numero = randint(limite_inferior, limite_superior)
    numero_ajustado = (numero // 3) * 3

    if numero_ajustado < limite_inferior:
        numero_ajustado = limite_inferior

    intento1 = int(input("Intente adivinar: "))

    if intento1 == numero_ajustado:
        print("Felicitaciones, adivino en el primer intento.")
    else:
        if intento1 < numero_ajustado:
            print("El numero es mayor.")
        else:
            print("El numero es menor.")

        intento2 = int(input("Intente de nuevo: "))

        if intento2 == numero_ajustado:
            print("Felicitaciones, adivino en su segundo intento.")
        else:
            if intento2 < numero_ajustado:
                print("El numero es mayor.")
            else:
                print("El numero es menor.")

            diferencia1 = numero_ajustado - intento1
            if diferencia1 < 0:
                diferencia1 = diferencia1 * -1

            diferencia2 = numero_ajustado - intento2
            if diferencia2 < 0:
                diferencia2 = diferencia2 * -1

            print("Te dare una pista:")
            if diferencia1 < diferencia2:
                print(
                    f"El numero que buscas esta mas cerca de {intento1} "
                    f"que de {intento2}"
                )
            elif diferencia2 < diferencia1:
                print(
                    f"El numero que buscas esta mas cerca de {intento2} "
                    f"que de {intento1}"
                )
            else:
                print(
                    f"El numero que buscas esta igual de cerca de {intento1} "
                    f"que de {intento2}"
                )

            intento3 = int(input("Intente la ultima vez: "))

            if intento3 == numero_ajustado:
                print("Felicitaciones, pudiste adivinar.")
            else:
                print("Perdiste.")
                print(f"El numero era: {numero_ajustado}")
