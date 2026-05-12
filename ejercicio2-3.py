num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2
division = num_1 / num_2
#ej 7//3 = 2
division_entera = num_1 // num_2
# ej 7%3 = 1
modulo = num_1 % num_2

potencia = num_1 ** num_2

print (f"Suma : {suma}", f"Resta: {resta}")
print (f"Multiplicacion: {multiplicacion}", f"Division: {division}")
print (f"Division entera: {division_entera}", f"Modulo: {modulo}")
print (f"Potencia: {potencia}")