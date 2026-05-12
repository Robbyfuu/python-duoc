OPERACIONES = {
    1: ("Suma", lambda x, y: x + y),
    2: ("Resta", lambda x, y: x - y),
    3: ("Multiplicación", lambda x, y: x * y),
    4: ("División", lambda x, y: x / y),
}


def mostrar_menu():
    print("\n============")
    print(" Calculadora")
    print("============")
    for num, (nombre, _) in OPERACIONES.items():
        print(f"  {num}) {nombre}")
    print("  5) Salir")
    print()


def leer_opcion():
    try:
        return int(input("Seleccione opción: "))
    except ValueError:
        return -1


def leer_numeros():
    while True:
        try:
            x = float(input("Ingrese primer número: "))
            y = float(input("Ingrese segundo número: "))
            return x, y
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")


def ejecutar_operacion(opcion, x, y):
    nombre, operacion = OPERACIONES[opcion]
    try:
        resultado = operacion(x, y)
        print(f"El resultado de la {nombre} es: {resultado}")
    except ZeroDivisionError:
        print("No se permite la división entre 0.")


def calculadora():
    mostrar_menu()
    while True:
        opcion = leer_opcion()

        if opcion == 5:
            print("Gracias por usar la calculadora.")
            break

        if opcion not in OPERACIONES:
            print("Opción no válida.")
            continue

        x, y = leer_numeros()
        ejecutar_operacion(opcion, x, y)


if __name__ == "__main__":
    calculadora()
