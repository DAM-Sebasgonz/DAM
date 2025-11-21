from random import randint

numero_aleatorio = randint(-50, 50)
turno = randint(1,2)
print(f"Se ha elegido el numero {numero_aleatorio}")
nro_usuario = int(input("Introduzca un numero del 1-10 -->"))
cantidad = numero_aleatorio - nro_usuario
numero = ""


while numero !=0:
    try:
        if numero_aleatorio < 0:
            numero = numero * -1 #Convertir a positivo
        if turno == 1:
            print(nro_usuario)
            print(f"Has ingresado el numero {nro_usuario}")
            break
        else:
            print(f"Le toca a la maquina")
            maquina_eleccion = randint(1,10)
            print(f"La maquina ha ingresado el numero {maquina_eleccion}")
            break
    except:
        print("Debe introducir un numero") 
else:
    print(f"Po po po... Has perdido")



