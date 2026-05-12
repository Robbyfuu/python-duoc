monto_retirar = int(input("Ingrese el monto a retirar: "))
billetes_10 = monto_retirar // 10000
resto10 = monto_retirar % 10000
print (f"Billetes de $10.000: {billetes_10}")
print (f"Resto: {resto10}")
billetes_5 = resto10 // 5000
resto5 = resto10 % 5000
print (f"Billetes de $5.000: {billetes_5}")
print (f"Resto: {resto5}")

# num1 % 2 = 0 si es par, 1 si es impar

billetes_2 = resto5 // 2000
resto2 = resto5 % 2000

print (f"Billetes de $2.000: {billetes_2}")
print (f"Resto: {resto2}")

billetes_1 = resto2 // 1000
resto1 = resto2 % 1000

print (f"Billetes de $1.000: {billetes_1}")