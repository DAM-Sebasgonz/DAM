'''Escribir un programa en Python que permita empaquetar una lista, donde 
empaquetar significa indicar la repetición de valores consecutivos mediante una tupla 
(valor, cantidad de repeticiones). Por ejemplo, empaquetar la lista [1, 1, 1, 3, 5, 1, 1, 3, 
3] debe generar la siguiente lista de tuplas: [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)]. 
 
Los elementos de la primera lista deben leerse por teclado.'''
#[(valor, cantidad de repeticiones)]
lista=[]
muestra=[]
while True:
    try:
        entrada=int(input("Escribe un nº para la lista entero: "))
    except:
        print("Error. Escribe un nº entero.")
    else:
        lista.append(entrada)
        while True:
            salir=input("¿Paramos? s/n: ").lower()
            if salir=='s':
                break
            elif salir=='n':
                break
            else:
                print("Opción incorrecta.")
                continue
        if salir=='s':
            break
        else:
            continue
print(f"La lista original: {lista}")
for elto in lista:
    if elto not in muestra:
        muestra.append(elto)
muestra.sort() #El ordenamiento ascendente es opcional, simplemente queda más visual.
aux_numeros=[]
for elto in muestra:
    aux_numeros.append(lista.count(elto))
solucion=[]
for i in range(len(muestra)):
    tupla=(muestra[i], aux_numeros[i])
    solucion.append(tupla)
print(solucion)
#Me creo una lista con valores, que pueden repetirse. 
#Me creo una lista filtrada con la muestra de cada uno de los valores sin repetir.
#Me creo otra lista para almacenar los valores repetidos que corresponden a cada valor de la muestra.
#Me creo la lista solución que contiene una tupla conformada por (muestra, n_repeticiones) por cada elemento de la muestra
