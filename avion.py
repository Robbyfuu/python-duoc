def mostrar_avion(): #Carlos Velasquez 
	print("  ",end="")
	for pos1 in range (1,34):
		print(str(pos1)+" ",end="")
	print("")
	for pos0 in range (6):
		print(chr(70-pos0)+" ",end="")
		for pos1 in range(33):
			if(pos1<8):
				print(str(asiento[pos0][pos1])+" ",end="")
			else:
				print (str(asiento[pos0][pos1])+"  ", end="")
		print("")
	print("  ",end="")
	for pos1 in range(1,34):
		if(pos1>=1) and (pos1<=5):
			print("E"+" ",end="")
		elif(pos1>=6) and (pos1<=8):
			print("N"+" ",end="")
		elif(pos1==9):
			print("N"+"  ",end="")
		elif(pos1>=10) and (pos1<=11):
			print("R"+"  ",end="")
		elif(pos1==12):
			print("E"+"  ",end="")
		elif(pos1>=13) and (pos1<=33):
			print("N"+"  ",end="")
	print("")
def Menu(): #Benjamin Jerez
	print("-------------  Menu  --------------")
	print("1. Compra de pasajes")
	print("2. Mostrar ubicaciones disponibles")
	print("3. Ver listado de Pasajeros")
	print("4. Buscar Pasajero")
	print("5. Reasignar asiento")
	print("6. Mostrar Ganancias Totales")
	print("7. Salir")
def Busca_rut(rut): #Esta función busca el rut ingresado por el usuario. Roberto Arce
	for i in range (cant_rut):
		isFound=False
		if(rut_personas[i]==rut):
			isFound=True
			break
	return isFound
def venta_rut(rut):  #Esta función busca el rut ingresado por el usuario. Roberto Arce
	for i in range (cant_rut):
		isFound=True
		if(rut_personas[i]==rut):
			isFound=False
			break
	return isFound

opcion=int(0)  # La inicialización de variables fue a medidas que se fue requiriendo
none=int(0)
Total_cont=int(0)
gananciatotal=int(0)
cont_E=int(0)
cont_N=int(0)
cont_R=int(0)
gananciatotal_E=int(0)
gananciatotal_N=int(0)
gananciatotal_R=int(0)
cant_rut=int(1)
asiento = [none] * 6
rut_personas=[0]
busca_rut=int(0)
reemplazo_rut=int(0)
cant_personas=int(0)
for i in range (0,6): # Roberto Arce linea 69 a 86
	asiento [i] = [none] * 33
while (opcion!=7):
	Menu()
	opcion=int(input("Seleccione una opcion: "))
	
	if(opcion==1):
		mostrar_avion()
		Total_cont=int(0)
		cant_boleto=int(input("Ingrese la cantidad de boletos que desea: "))
		contador_while=int(0)
		cant_personas=cant_personas+cant_boleto
		if (cant_personas<=198):
			if(cant_boleto<=198):
				cant_personas=cant_personas-cant_boleto
				while(contador_while<cant_boleto):
					rut=int(input("Ingrese el RUT de la persona sin DV: "))
					
					if(venta_rut(rut)):
						rut_personas.append(rut)
						cant_rut=cant_rut+1
						ingreso_fila=int(0)
						ingreso_columna=int(0)
						while (ingreso_fila<1): #Benjamin Jerez linea  87-116
							in_filas = str(input("Por favor ingresar la letra de la fila (A-F) ")) 
							filas=in_filas.upper()
							if (filas=='A'): 
								fila=ord(filas)-59
								ingreso_fila=ingreso_fila+1
							elif(filas=='B'):
								fila= ord(filas)-61
								ingreso_fila=ingreso_fila+1
							elif(filas=='C'):
								fila= ord(filas)-63
								ingreso_fila=ingreso_fila+1
							elif(filas=='D'):
								fila= ord(filas)-65
								ingreso_fila=ingreso_fila+1
							elif(filas=='E'):
								fila= ord(filas)-67
								ingreso_fila=ingreso_fila+1
							elif(filas=='F'):
								fila= ord(filas)-69
								ingreso_fila=ingreso_fila+1
							
							else:
								print("La fila ingresada no es valida")
						while(ingreso_columna<1):				
							columna = int(input("Por favor ingresar el numero de columna(1-33) "))
							if(columna>=1) and (columna<=33):
								ingreso_columna=ingreso_columna+1
							else:
								print("La columna ingresada no es valida")

						if(asiento[fila - 1][columna - 1] ==0):# Carlos Velazquez linea 118 a 149
							cant_personas=cant_personas+1
							contador_while=contador_while+1

							asiento[fila-1][columna - 1] = "X"
							if(columna>=1) and (columna<=5):
								valorasiento=80000
								gananciatotal_E=gananciatotal_E+valorasiento
								cont_E=cont_E+1
							elif(columna>=6) and (columna<=9):
								valorasiento=60000
								gananciatotal_N=gananciatotal_N+valorasiento
								cont_N=cont_N+1
							elif(columna>=10) and (columna<=11):
								valorasiento=50000
								gananciatotal_R=gananciatotal_R+valorasiento
								cont_R=cont_R+1
							elif(columna==12):
								valorasiento=80000
								gananciatotal_E=gananciatotal_E+valorasiento
								cont_E=cont_E+1
							elif(columna>=13) and (columna<=33):
								valorasiento=60000
								gananciatotal_N=gananciatotal_N+valorasiento
								cont_N=cont_N+1
							Total_cont=cont_E+cont_N+cont_R
							gananciatotal=gananciatotal_E+gananciatotal_N+gananciatotal_R
							print ("Reserva Exitosa")
						else:
							rut_personas.remove(rut)
							cant_rut=cant_rut-1
							print ("Asiento Ocupado")
					else:
						print("El RUT ingresado se encuentra registrado")

				mostrar_avion()
	elif(opcion==2): #Benjamin Jerez linea 154 a 162
		mostrar_avion()
	elif(opcion==3):
		for rut1 in range(cant_rut):
			print(" ",end="")
			if(rut_personas[rut1]!=0):
				rut_personas.sort()
				print(str(rut_personas[rut1]))
			elif(cant_rut==1):
				print("No existen pasajeros registrados")
	elif(opcion==4): #Carlos Velazquez linea 163 a 168
		rut=int(input("Ingrese el RUT de la persona sin DV: "))
		if(Busca_rut(rut)):
			print("RUT encontrado")
		else:
			print("RUT no encontrado")
	elif(opcion==5): #Roberto Arce linea 169 a 181
		reemplazo_rut=int(input("Ingrese el RUT que desea reemplazar: "))
		if(Busca_rut(reemplazo_rut)):
			rut_personas.remove(reemplazo_rut)
			cant_rut=cant_rut-1
			nuevo_rut=int(input("Ingrese el nuevo RUT a registrar: "))
			if(nuevo_rut not in rut_personas):
				rut_personas.append(nuevo_rut)
				cant_rut=cant_rut+1
			else:
				cant_rut=cant_rut+1
				print("El RUT ya se encuentra registrado")
				rut_personas.append(reemplazo_rut)
		else:
			print("El RUT ingresado no se encuentra en el sistema")					
	elif(opcion==6): # Benjamin Jerez linea 182 a 188
		print("--------------------  Ganancias Totales  ------------------------")
		print("Tipo de Asiento             "+"      Cantiadad           "+"Total")
		print("Asiento Común        $60.000          "+str(cont_N)+"             $"+str(gananciatotal_N))
		print("Espacio para piernas $80.000          "+str(cont_E)+"             $"+str(gananciatotal_E))
		print("No reclina           $50.000          "+str(cont_R)+"             $"+str(gananciatotal_R))
		print("TOTAL                                 "+str(Total_cont)+"             $"+str(gananciatotal))
