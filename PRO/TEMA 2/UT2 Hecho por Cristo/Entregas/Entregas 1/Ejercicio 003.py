'''Se quiere simular un juego en el que participan N jugadores y otra persona que
hace de árbitro. Cada jugador elige 4 números en el rango [1, 10], pudiendo estar
repetidos. A continuación, el árbitro, sin conocer los números que ha elegido cada
jugador, selecciona 2 números A y B.
 

El programa debe ser capaz de calcular cuántos números de los seleccionados
por cada jugador están comprendidos entre los valores A y B. Ganará el jugador
que más números tenga en dicho intervalo.
 
Se pide implementar un programa modular que simule el juego para 3 jugadores,
teniendo en cuenta que:

Tanto los 4 datos de cada jugador, como los valores para A y B se introducirán por
teclado. 

En todos los casos, el programa detectará la entrada de números
erróneos, solicitando nuevamente el dato hasta que sea válido.

Se deben mostrar por pantalla no solo los aciertos de cada jugador sino los datos
que ha introducido cada jugador y los que ha seleccionado el árbitro. Por último,
hay que imprimir la media aritmética de los aciertos de todos los jugadores'''

jugador_1=[]
jugador_2=[]
jugador_3=[]
ocurrencias_1=0
ocurrencias_2=0
ocurrencias_3=0

arbitro=[]
while True:
    #preguntamos al j1 por sus nº:
    while len(jugador_1)<4:
        try:
            numero = int(input(f"Jugador 1, introduce un número (entre 1 y 10): "))
            if 1<=numero<=10:
                jugador_1.append(numero)
            else:
                print("Número incorrecto, introduce un número entre 1 y 10.")
        except:
            print("Debes introducir un número.")
    #preguntamos al j2 por sus nº:
    while len(jugador_2)<4:
        try:
            numero = int(input(f"Jugador 2, introduce un número (entre 1 y 10): "))
            if 1<=numero<=10:
                jugador_2.append(numero)
            else:
                print("Número incorrecto, introduce un número entre 1 y 10.")
        except:
            print("Debes introducir un número.")
    #preguntamos al j3 por sus nº:
    while len(jugador_3)<4:
        try:
            numero = int(input(f"Jugador 3, introduce un número (entre 1 y 10): "))
            if 1<=numero<=10:
                jugador_3.append(numero)
            else:
                print("Número incorrecto, introduce un número entre 1 y 10.")
        except ValueError:
            print("Debes introducir un número.")
    #preguntamos al árbitro por sus nº:
    while len(arbitro)<2:
        try:
            numero_A = int(input("Árbitro, introduce un número A (entre 1 y 10): "))
            numero_B = int(input("Árbitro, introduce un número B (entre 1 y 10): "))
            if 1<=numero_A<=10 and 1<=numero_B<=10 and numero_A!=numero_B:
                arbitro.append(numero_A)
                arbitro.append(numero_B)
                arbitro.sort()#*
            else:
                print("Número incorrecto, introduce un número A y B entre 1 y 10, y distintos.")
        except:
            print("Debes introducir un número.")
    break

    #comprobamos las ocurrencias de cada lista comparando con el árbitro:
#En esta primera parte del programa buscamos preguntar a los jugadores simulados por sus cuatro nº. Luego se pregunta al árbitro por los valores de A y B. 
#Nota: Si alguno de los jugadores o el propio árbitro se equivoca al introducir un dato, salta a otra iteración hasta que introduzca el dato correctamente. 
#* Con sort ordenamos los datos del árbitro para que siempre el intervalo sea desde el menor de los nº hasta el mayor. 

for numero in jugador_1:
    if arbitro[0]<=numero<=arbitro[1]:
        ocurrencias_1+=1
for numero in jugador_2:
    if arbitro[0]<=numero<=arbitro[1]:
        ocurrencias_2+=1
for numero in jugador_3:
    if arbitro[0]<=numero<=arbitro[1]:
        ocurrencias_3+=1

#En esta siguiente parte del programa los jugadores obtienen puntos si los nº se encuentran dentro del intervalo AB.

#casos donde los jugadores ganan
if ocurrencias_1>ocurrencias_2 and ocurrencias_1>ocurrencias_3:
    print(f"El jugador 1 ha ganado con {ocurrencias_1} ocurrencias.")
elif ocurrencias_2>ocurrencias_1 and ocurrencias_2>ocurrencias_3:
    print(f"El jugador 2 ha ganado con {ocurrencias_2} ocurrencias.")
elif ocurrencias_3>ocurrencias_1 and ocurrencias_3>ocurrencias_2:
    print(f"El jugador 3 ha ganado con {ocurrencias_3} ocurrencias")
#casos donde los jugadores empatan
else:
    if ocurrencias_1==ocurrencias_2==ocurrencias_3:
        print(f"Empate global. Jugador 1: {ocurrencias_1} ocurrencias | Jugador 2: {ocurrencias_2} ocurrencias| Jugador 3: {ocurrencias_3} ocurrencias")
    elif ocurrencias_1==ocurrencias_2:
        print(f"Jugador 1 y 2 empatan.")
    elif ocurrencias_1==ocurrencias_3:
        print(f"Jugador 1 y 3 empatan.")
    elif ocurrencias_2==ocurrencias_3:
        print(f"Jugador 2 y 3 empatan.")
#mostramos los resultados finalmente
print(f"Jugador 1: {jugador_1}, A - B: [{arbitro[0]},{arbitro[1]}], Ocurrencias: {ocurrencias_1}")
print(f"Jugador 2: {jugador_2}, A - B: [{arbitro[0]},{arbitro[1]}], Ocurrencias: {ocurrencias_2}")
print(f"Jugador 3: {jugador_3}, A - B: [{arbitro[0]},{arbitro[1]}], Ocurrencias: {ocurrencias_3}")
#calculamos la media de los aciertos:
media_aciertos=(ocurrencias_1+ocurrencias_2+ocurrencias_3)/3
print(f"La media de los aciertos de todos los jugadores es: {media_aciertos}")
