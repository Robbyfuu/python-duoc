valor_medicamentos = 60000
valor_despacho = 8000

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ").upper()

descuento_medicamentos = 0
descuento_despacho = 0

if edad <= 30:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 18
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 12
elif edad < 60:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 12
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 8
else:
    descuento_medicamentos = 0

if tramo == "A" or tramo == "B":
    descuento_despacho = 10
    if edad >= 55:
        descuento_despacho = descuento_despacho + 5
else:
    descuento_despacho = 0

valor_final_medicamentos = valor_medicamentos - (
    valor_medicamentos * descuento_medicamentos // 100
)
valor_final_despacho = valor_despacho - (
    valor_despacho * descuento_despacho // 100
)

print(f"El valor de medicamentos es: {valor_final_medicamentos}")
print(f"El valor del despacho es: {valor_final_despacho}")
