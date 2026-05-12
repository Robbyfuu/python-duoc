# tipo de dato entero
edad = 20 # or edad: int = 20 

# tipo de dato con decimal (float)
altura = 1.75 # or altura: float = 1.75

# tipo de dato cadena de texto (string)
nombre = "Anthony" # or nombre: str = "Anthony"

# tipo de dato booleano (bool)
# anthony_estudia = True # or anthony_estudia: bool = False
# contador :int = 0
# while True: 
#     print("Anthony estudia")
#     contador += 1
#     if contador == 3:
#         print("Anthony ya no estudia")
#         #anthony_estudia = False
#         break # el break sirve para salir del while
#     print(f"Anthony estudio {contador} veces")
#     continue # el continue sirve para saltar a la siguiente iteración del while
# print(f"Anthony estudio {contador} veces")


# tipos de input's
# por defecto, input devuelve un string
nombre_completo = input("Ingrese su nombre completo: ")

#entonces para poder recibir un numero, debemos convertir el input a un entero
# y este se convierte con la funcion int(),
# que envuelve el input y lo convierte a un entero
edad = int(input("Ingrese su edad: "))

# entonces para poder recibir un numero con decimal, debemos convertir el input a un flotante
# y este se convierte con la funcion float(),
# que envuelve el input y lo convierte a un flotante
altura = float(input("Ingrese su altura: "))

# entonces para poder recibir un booleano, debemos convertir el input a un booleano
# y este se convierte con la funcion bool(),
# que envuelve el input y lo convierte a un booleano
# cuando nosotros ingresamos 0 o 1, se convierte a False o True respectivamente
# esto no es muy util, ya que nosotros podemos ingresar True o False directamente
altura = bool(input("Ingrese su altura: "))

# para imprimir solo un texto 
print ("Hola")

# si nosotros queremos imprimir un valor de una variable
# podemos usar el f-string, que es una forma de interpolar variables en un string
# f-string es una forma de interpolar variables en un string
print (f"Hola {nombre_completo}, tienes {edad} años y tu altura es {altura} ")
# o
# cuando utilizamos la coma se le agrega un espacio entre el texto y el valor de la variable
print ("Hola", nombre_completo, "tienes", edad, "años")
#o, podemos usar el + para concatenar strings
print ("Hola " + nombre_completo)
