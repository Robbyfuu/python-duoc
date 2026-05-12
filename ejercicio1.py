from random import randint
RANG_START=1
RANG_STOP=100
CONT_INCREMENTO= 1
numero_secreto = randint(RANG_START,RANG_STOP)
MAX_INTENTOS = 7
cont_intentos = 1
no_adivino = True
mensaje = ""
print(f"Adivina el número secreto (entre {RANG_START} y {RANG_STOP}). Tienes {MAX_INTENTOS} intentos. ")
while cont_intentos <= MAX_INTENTOS and no_adivino :
    try:
        ingreso = int(input(f"Intento {cont_intentos}: "))
    except ValueError:
        print(f"el dato ingresado debe ser un número({RANG_START} y {RANG_STOP})")
        continue
    if ingreso > numero_secreto:
        mensaje = "Muy alto, intenta con un número menor"
    elif (ingreso < numero_secreto):
        mensaje = "Muy bajo, intenta con un número mayor"
    else :
        mensaje = (f"¡Felicidades! Adivinaste en {cont_intentos} intentos")
        no_adivino=False
    print(mensaje)
    cont_intentos += CONT_INCREMENTO

if cont_intentos > MAX_INTENTOS and no_adivino:
    print(f"Perdiste. El número secreto era: {numero_secreto}")

