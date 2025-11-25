'''
Escriba un programa en Python para comprobar si la lista contiene tres números 
comunes consecutivos.
Lista : [4, 5, 5, 5, 3, 8]
La salida debe ser [5]
Lista : [1, 1, 1, 64, 23, 64, 22, 22, 22]
La salida debe ser: [1,22]'''
lista=[]
consecutivos=[]
while True:
    ingreso = input("Ingresa un nº o *fin para salir: ")
    if ingreso == '*fin':
        break
    try:
        numero = int(ingreso) 
        lista.append(numero)
    except:
        print("No es un nº. Prueba otra vez")
#recorremos la lista de elementos construida con los datos del usuario. Queremos recorrer la lista por la longitud
#-2 para no salirnos del rango al comparar.
for elto in range(len(lista)-2):
    if lista[elto] == lista[elto+1] == lista[elto+2]:
        if lista[elto] not in consecutivos:
            consecutivos.append(lista[elto])
print(f"Números de la lista: {lista}")
print(f"Números consecutivos en la lista: {consecutivos}")

#el usuario introduce nº hasta que escribe *fin y se almacenan en una lista. 
#se recorre la lista buscando que los números en las posiciones x,x+1 y x+2 sean iguales. Si lo son, se añade a la lista consecutivos sin repetirse.
