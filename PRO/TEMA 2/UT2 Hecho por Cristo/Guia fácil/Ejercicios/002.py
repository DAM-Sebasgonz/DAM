'''Escriba un programa en Python que dada una lista de números enteros, obtenga otra lista donde 
se eliminen los duplicados. Mantenga el orden de los números en la nueva lista generada. 
Ejemplos de como debe ser la salida del programa debe ser como la que se muestra a 
continuación: 
[2, 3, 2, 2, 1, 5, 4, 2, 4, 9] -> [2, 3, 1, 5, 4, 9] 
[0, 3, 0, 3, 0, 3] -> [0,3] 
[1, 2, 3, 4, 5, 4, 3, 2, 1] -> [1, 2, 3, 4, 5] '''
lista=[]
lista_filtrada=[]
while True:
    numero=input("Introduce un nº entero o escriba @ para salir: ")
    if numero == "@":
        break
    try:
        numero=int(numero)
        lista.append(numero)
    except:
        print("Introduce un número entero.")

for numero in lista:
    if numero not in lista_filtrada:
        lista_filtrada.append(numero)

print(lista_filtrada) 