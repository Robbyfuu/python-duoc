from random import randint
numero_secreto = randint(1, 10)
intentos = 0
contador = 0

while True: 
    intentos = int(input("Ingrese un numero (1-10): ")) 
    contador += 1

    if intentos == numero_secreto:
        print("Felicitaciones, adivinaste el numero secreto")
        break
    else:
        if( intentos > numero_secreto):
            print("El numero es menor")
        else:
            print("El numero es mayor")
print (f"Adivinaste el numero secreto en {contador} intentos")