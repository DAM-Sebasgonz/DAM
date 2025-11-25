'''Dada una lista, extraer todos los elementos cuya frecuencia sea superior a n. Los
elementos de la lista deben leerse mediante un bucle del cual se sale con la
secuencia *fin.
Posteriormente se debe leer el valor de n.
Ejemplos
Lista = [4, 6, 4, 3, 0, 3, 4, 3, 0, 4, 3, 8], n = 3 

La salida debe ser [4,3]
Lista = [4, 6, 4, 5, 3, 3, 4, 3, 4, 1, 6, 6], n = 2
La salida debe ser [4, 3, 6] 
'''
lista=[]
lista_auxiliar=[]
while True:
    ingreso = input("Ingresa un nº o *fin para salir: ")
    if ingreso == '*fin':
        break
    try:
        numero = int(ingreso)
        lista.append(numero)
    except:
        print("No es un nº. Prueba otra vez")
try:
    n=int(input("Escribe un valor de 'n': "))
except:
    print("No es un nº. Prueba otra vez")
else:
    for elto in lista:
        if lista.count(elto)>n:
            if elto not in lista_auxiliar:
                lista_auxiliar.append(elto)
    print(lista_auxiliar)

#pedimos al usuario nº hasta que teclee *fin - se almacenan en una lista
#pedimos al usuario un valor para n 
#recorremos la lista con los nº introducidos por el usuario y ponemos la condición de que si la frecuencia del elemento
#es mayor que el valor de n introducido por el usuario lo guarde en una lista aparte y sin repeticiones.

        
