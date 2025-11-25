'''Realizar un programa que dado dos listas, verifique que las listas estén 
solapadas o no. Una lista está solapada con otra, cuando hay un elemento común entre las 
dos listas. El programa escribirá como salida si las listas están solapadas o no. Las listas 
de prueba se deben escribir en el código del problema. 
 
Ejemplo, sean A, B y C las siguientes listas: 
 
A = [1, 2, 3, 4] 
B = [5, 6, 7, 8, 9] 
C = [2, 0, 9] 
 
Las listas A y B no están solapadas, en cambio, las listas A y C si están solapadas, el 
elemento 2 es común a las 2.'''
lista1=[]
lista2=[]
solapadas=False
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
#comprobar solapamiento de listas: 
for elto in lista1:
    if elto in lista2:
        print(f"Las listas A={lista1} y B={lista2} están solapadas.")
        solapadas=True
        break
    else:
        continue
if not solapadas:
    print(f"Las listas A={lista1} y B={lista2} NO están solapadas.")
