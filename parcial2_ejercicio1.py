valor_mensualidad = 160000
valor_matricula = 35000

horas_diarias = int(input("Ingrese horas diarias: "))
tramo = input("Ingrese tramo (A, B, C o D): ").upper()

descuento_mensualidad = 0
descuento_matricula = 0

if horas_diarias >= 8:
    if tramo == "A" or tramo == "B":
        descuento_mensualidad = 20
    elif tramo == "C" or tramo == "D":
        descuento_mensualidad = 14
elif horas_diarias >= 4:
    if tramo == "A" or tramo == "B":
        descuento_mensualidad = 12
    elif tramo == "C" or tramo == "D":
        descuento_mensualidad = 8
else:
    descuento_mensualidad = 0

if tramo == "A" or tramo == "B":
    descuento_matricula = 10
    if horas_diarias >= 6:
        descuento_matricula = descuento_matricula + 5
else:
    descuento_matricula = 0

valor_final_mensualidad = valor_mensualidad - (
    valor_mensualidad * descuento_mensualidad // 100
)
valor_final_matricula = valor_matricula - (
    valor_matricula * descuento_matricula // 100
)

print(f"El valor de la mensualidad es: {valor_final_mensualidad}")
print(f"El valor de la matricula es: {valor_final_matricula}")
