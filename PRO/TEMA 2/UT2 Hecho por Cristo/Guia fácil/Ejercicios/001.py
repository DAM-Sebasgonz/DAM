'''Escriba un programa en Python que dada una lista de valores numéricos enteros  obtenga su 
máximo valor.  En este ejercicio no se puede usar los métodos max() y sorted(). 
Ejemplos: 
La salida debe mostrarse como se muestra a continuación. 
[ 3, 7, 100, 2, -20] -> 100 
[200, -100, 4, 8, 200] -> 200 
[-7, -10, -6, -3] -> -3'''
lista=[]
while True:
    numero=input("Introduce un nº entero o escriba @ para salir: ")
    if numero == "@":
        break
    try:
        numero=int(numero)
        lista.append(numero)
    except:
        print("Introduce un número entero.")
maximo = lista[0]
for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
print("El máximo valor de la lista es:",maximo)


#echar un vistazo en casa y comprender. Crear nuevos programas y variantes. Practicar.