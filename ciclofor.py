import random
contador = 0
x = random.randint(1, 10)
primer_intento= 0
while contador < 3:
    if (contador == 0):
        a = int(input("Intente adivinar:  "))
        primer_intento = a
    elif(contador == 1):
        if(a> x): 
            print("El numero es menor")
        else:
            print("El numero es mayor")
        a = int(input("Intente nuevamente:  "))
    else:
        z = x - primer_intento
        y = z - a
        if( z> y):
            print(f"El numero que buscas esta mas cerca {a} que del {primer_intento}")
        else:
            print(f"El numero que buscas esta mas cerca {primer_intento} que del {a}")
        a = int(input("Intente la ultima vez:  "))
    if (x == a):
        if(contador == 0):
            print("Felicitaciones, adivino en el primer intento")
        elif(contador == 1):
            print("Felicitaciones, adivino en el segundo intento")
        else:
            print("Felicitaciones, pudiste adivinar")
        break
    else:
        print("No adivinaste el numero")
        contador += 1
        continue
      
