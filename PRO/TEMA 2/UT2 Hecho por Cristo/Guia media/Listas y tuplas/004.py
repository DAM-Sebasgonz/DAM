'''Queremos guardar en una lista los nombres y las edades de los alumnos de 
un curso. Realiza un programa que permita leer el nombre y la edad de cada alumno y 
forme la lista solicitada.

El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco 
(*). 
 
La lista debe ser de tuplas, y cada tupla contiene (nombre_del_alumno, edad) 
 
Al finalizar la lectura de los datos el programa debe mostrar la siguiente información:  
• Los nombres de los alumnos mayores de edad. 
• Los nombres y edades de los 3 alumnos mayores.'''

#creación de la tabla alumnos para organizar la lectura:

alumnos=[]

#en un ciclo while, preguntaremos indefinidamente por nombre y edad de un alumno y convertiremos dichos datos en tuplas. La condición
#de parada del ciclo while es tener '*' en un nombre.

while True:
    nombre=input("Introduzca el nombre del alumno (o * para salir): ")
    if nombre=='*':
        break
    edad=int(input("Introduzca la edad del alumno: "))
    alumnos.append((nombre,edad))#creamos la tupla y la añadimos usando append en la tabla alumnos.
print(alumnos)
#en este punto ya tenemos la tabla con todos los alumnos, ahora podemos filtrar y mostrar la información solicitada:
for elto in range(len(alumnos)):
    nombre, edad=alumnos[elto] #pasamos los parámetros / nombre(en tupla elemento 0) edad (en tupla elemento 1)
    if edad>18:
        print(f"El alumno {nombre} es mayor de edad.")
#para filtrar los 3 alumnos mayores a partir de la lista alumnos:
for i in range(len(alumnos)):
    for j in range(0, len(alumnos) - i - 1):
        if alumnos[j][1] < alumnos[j + 1][1]:  # Comparar por el segundo elemento
            alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]  # Intercambiar

print(alumnos)