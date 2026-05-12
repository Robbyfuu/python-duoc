sw = 1
notas = []
while sw ==1:
    print("------SISTEMA DE NOTAS------")
    print("1. Agregar nota")
    print("2. Ver todas las notas")
    print("3. Ver promedio")
    print("4. Borrar ultima nota")
    print("5. Salir")

    try:
         op = int(input("Selecciona una opcion: "))
    except ValueError:
        print("Error: ingresa un numero.")
        continue
         
    if op == 1:
        nota = float(input("Ingrese una nota entre (1.0 y 7.0): "))
        if 1.0 <= nota <= 7.0:
             notas.append (nota)
             print("Nota agregada.")
        else: print("La nota debe ser entre 1.0 y 7.0")
          
    elif op == 2:
        if len(notas) > 0:
            print("Notas: ", notas)
        else:
            print("No hay notas ingresadas.")

    elif op == 3:
        if len(notas) > 0:
            promedio = sum(notas) / len(notas)
            print("Promedio: ", round(promedio, 2))
        else: 
            print("No hay notas ingresadas.")

    elif op == 4: 
        if len(notas) > 0:
            print("nota eliminada: ", notas.pop())
        else: 
            print("No hay notas para borrar")
    elif op == 5:
        print("Saliendo del programa...")
        sw = 0
        
    else:
        print("opcion invalida.")