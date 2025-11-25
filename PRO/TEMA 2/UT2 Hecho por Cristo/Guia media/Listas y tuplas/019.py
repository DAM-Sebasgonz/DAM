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
#mainloop
while True:
    #preguntamos al j1 por sus nº:
    while len(jugador_1)<4:
        try:
            numero = int(input(f"Jugador 1, introduce un número (entre 1 y 10): "))
            if 1<=numero<=10:
                jugador_1.append(numero)
            else:
                print("Número incorrecto, introduce un número entre 1 y 10.")
        except ValueError:
            print("Debes introducir un número.")
    #preguntamos al j2 por sus nº:
    while len(jugador_2)<4:
        try:
            numero = int(input(f"Jugador 2, introduce un número (entre 1 y 10): "))
            if 1<=numero<=10:
                jugador_2.append(numero)
            else:
                print("Número incorrecto, introduce un número entre 1 y 10.")
        except ValueError:
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
            else:
                print("Número incorrecto, introduce un número A y B entre 1 y 10, y distintos.")
        except ValueError:
            print("Debes introducir un número.")
    break

    #comprobamos las ocurrencias de cada lista comparando con el árbitro:
for numero in jugador_1:
    if numero in arbitro:
        ocurrencias_1+=1
for numero in jugador_2:
    if numero in arbitro:
        ocurrencias_2+=1
for numero in jugador_3:
    if numero in arbitro:
        ocurrencias_3+=1
    #mostramos los resultados:
print(f"Jugador 1: {jugador_1}, A y B: {arbitro}, Ocurrencias: {ocurrencias_1}")
print(f"Jugador 2: {jugador_2}, A y B: {arbitro}, Ocurrencias: {ocurrencias_2}")
print(f"Jugador 3: {jugador_3}, A y B: {arbitro}, Ocurrencias: {ocurrencias_3}")
#calculamos la media de los aciertos:
media_aciertos=(ocurrencias_1+ocurrencias_2+ocurrencias_3)/3
print(f"La media de los aciertos de todos los jugadores es: {media_aciertos}")
