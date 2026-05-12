edad = int(input("Ingrese su edad: "))
nombre = input("Ingrese su nombre: ")

# =============================================
# AND: ambas condiciones deben ser verdaderas
# =============================================
# Ejemplo: descuento solo para jóvenes llamados "admin"

if edad < 30 and nombre == "admin":
    print("Tienes acceso con descuento especial")
    #  edad < 30  | nombre == "admin" | resultado
    #  True       | True              | True  ✅
    #  True       | False             | False ❌
    #  False      | True              | False ❌
    #  False      | False             | False ❌

# =============================================
# OR: basta que UNA condición sea verdadera
# =============================================
# Ejemplo: entrada gratis para niños O adultos mayores

if edad < 12 or edad >= 65:
    print("Entrada gratis")
    #  edad < 12  | edad >= 65  | resultado
    #  True       | False       | True  ✅
    #  False      | True        | True  ✅
    #  False      | False       | False ❌
    #  True       | True        | (imposible, pero sería True)

# =============================================
# Combinando AND y OR
# =============================================
# Ejemplo: clasificación de edad + nombre

if edad < 18:
    print(f"{nombre}, eres menor de edad")
elif 18 <= edad <= 40 and (nombre == "ana" or nombre == "luis"):
    print(f"{nombre}, eres adulto joven con nombre reconocido")
elif 18 <= edad <= 40:
    print(f"{nombre}, eres adulto joven")
elif 41 <= edad < 65:
    print(f"{nombre}, eres adulto")
else:
    print(f"{nombre}, eres adulto mayor")
