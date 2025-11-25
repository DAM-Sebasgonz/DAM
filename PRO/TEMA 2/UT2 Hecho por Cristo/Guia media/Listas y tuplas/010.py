'''Ejercicio 10: Diseñe un programa que cree tres listas ‘lista1’, ‘lista2’ y ‘lista3’. 
 
La lista1 y lista2 se llenan con números que se leen por teclado. 
Las lista3 contiene la suma elemento por elemento de lista1 y lista2. 
Al final el programa debe mostrar el resultado de la siguiente forma: 
 
nro1lista1 + nro1lista2 = nro1lista3 
nro2lista1 + nro2lista2 = nro2lista3 
nro3lista1 + nro3lista2 = nro3lista3 
nro4lista1 + nro4lista2 = nro4lista3 
nro5lista1 + nro5lista2 = nro5lista3 
 
La lista 1 es = [nro1lista1, nro2lista1, nro3lista1, nro4lista1, nro5lista1] 
La lista 2 es = [nro1lista2, nro2lista2, nro3lista2, nro4lista2, nro5lista2] 
La lista 3 es = [nro1lista3, nro2lista3, nro3lista3, nro4lista3, nro5lista3]'''
lista1=[]
lista2=[]
lista3=[]
while True:
    lista_1=input("Escriba un nº para la lista 1 o @ para salir: ")
    if lista_1=='@':
        break
    try:
        lista_1=int(lista_1)
        lista1.append(lista_1)
    except:
        print("No es un nº válido. Introduce un nº entero.")
while True:
    lista_2=input("Escriba un nº para la lista 2 o @ para salir: ")
    if lista_2=='@':
        break
    try:
        lista_2=int(lista_2)
        lista2.append(lista_2)
    except:
        print("No es un nº válido. Introduce un nº entero.")
# Verificamos que ambas listas tengan la misma cantidad de elementos
if len(lista1) != len(lista2):
    print("Error: Ambas listas deben tener la misma cantidad de elementos.")
else:
    # Calculamos la lista 3 como la suma elemento por elemento
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        lista3.append(suma)
        print(f"{lista1[i]} + {lista2[i]} = {suma}")
print(f"La lista 1 es {lista1}\nLa lista 2 es {lista2}\nLa lista 3 es {lista3}")
