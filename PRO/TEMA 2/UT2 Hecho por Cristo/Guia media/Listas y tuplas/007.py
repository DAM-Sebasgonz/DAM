'''Se quiere realizar un programa que lea por teclado y almacene en una lista 
las 9 notas obtenidas por un alumno en las asignaturas que está cursando (comprendidas 
entre 0 y 10).  
 
Se debe verificar que la nota esté entre 0 y 10, en caso de que no se cumpla, se debe 
indicar un mensaje al usuario indicando el error. Al tercer error, al indicar la misma nota, 
se debe abortar la ejecución del programa. 
 
Una vez leídas las notas, el programa debe mostrarlas todas, calcular e imprimir la nota 
media , la nota mayor y menor que haya obtenido. 
 
La forma de la salida debe ser la siguiente: 
 
Notas obtenidas: nota1, nota2, nota3, nota4 nota5, nota6 nota7, nota8, nota9 
 
Promedio de notas: ***** 
Nota más alta: ***** 
Nota más baja: *****'''
boletin=[]
notas=9
intentos=0
while True:
    while notas>0 and intentos<3:
        try:
            notas_obtenidas=int(input("Introduce una nota válida entre 0 y 10: "))
        except:
            print("Introduce un número válido.")
            intentos+=1
            continue
        if notas_obtenidas<0 or notas_obtenidas>10:
            print("La nota debe estar entre 0 y 10.")
            intentos+=1
            continue
        if notas_obtenidas>=0 or notas_obtenidas<=10:
            boletin.append(notas_obtenidas)
            notas-=1
    if intentos==3:
        exit()
    else:
        maximo=max(boletin)
        maximo=maximo*'*'
        minimo=min(boletin)
        minimo=minimo*'*'
        promedio=sum(boletin)/len(boletin)
        promedio=round(promedio)*'*'
        print(f"boletin de alumno > {boletin}\nNota máxima: {maximo}\nNota mínima: {minimo}\nPromedio: {promedio}")
        break

            
