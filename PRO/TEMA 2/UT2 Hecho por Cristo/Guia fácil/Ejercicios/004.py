'''Escribir un programa en Python que dada una lista de elementos, genere otra lista eliminando los 
elementos duplicados consecutivos.  
Ejemplos: 
La lista  [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4] debe dar como resultado la lista [0, 1, 2, 3, 4, 5, 
6, 7, 8, 9, 4] y con la lista ['a', 'b', 'b', 'b', 'c', ‘b’] debe dar ['a', 'b', 'c', 'b']'''

lista=[]
lista_sec=[]
while True:
    entrada=input("Introduzca nº en la lista hasta que escriba @ para salir: ")
    if entrada=='@':
        break
    else:
        if entrada.isdigit():
            lista.append(int(entrada))
            continue
        else:
            lista.append(entrada)
            continue
for i in range(len(lista)):
    if i==0 or lista[i]!=lista[i-1]:
        lista_sec.append(lista[i])
print(lista_sec)