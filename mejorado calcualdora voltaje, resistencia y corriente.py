prefijos = {
    "micro": 0.000001,
    "mili": 0.001,
    "kilo": 1000,
    "mega": 1000000,
}


def pedir_valor(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("valor inválido, ingrese un número")

# la fun
def pedir_prefijo(mensaje):
    while True:
        prefijo = input(mensaje).lower()
        if prefijo in prefijos:
            return prefijos[prefijo]
        print(f"prefijo inválido, opciones: {', '.join(prefijos)}")

def menu ():
    print("""
    1) voltaje
    2) resistencia
    3) corriente
    4) salir
          """)

while True:
    menu()
    opcion = input("ingrese una opcion: ")
    match opcion:
        case "1":
            valor_resi = pedir_valor("ingrese el valor de la resistencia: ")
            mult_resi = pedir_prefijo("ingrese el prefijo de la resistencia (micro, mili, kilo, mega): ")
            valor_corri = pedir_valor("ingrese el valor de la corriente: ")
            mult_corri = pedir_prefijo("ingrese el prefijo de la corriente (micro, mili, kilo, mega): ")
            resistencia = valor_resi * mult_resi
            corriente = valor_corri * mult_corri
            voltaje = resistencia * corriente
            print(f"el voltaje es: {voltaje} V")
