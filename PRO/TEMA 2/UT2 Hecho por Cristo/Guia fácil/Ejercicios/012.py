'''Ejercicio 012:
Escriba un programa en Python que pida al usuario un nombre y apellidos en el formato
"apellidos, nombre” e imprima las iniciales de dicha persona pasadas a mayúsculas y con punto
al final.
A tener en cuenta:
El nombre puede tener uno o dos elementos.
El apellido puede tener uno o dos elementos.
Ejemplos:
‘Pérez Ramírez, jesús’ -> J.P.R.
´garcía, Marta’ -> M.G.
‘Perez rodríguez, María josé’ -> M.J.P.R '''
#separar por espacio y eliminar la coma para operar bien
lista_auxiliar=[]
nombre=input("Escriba un nombre: ")
nombre=nombre.replace(',','')
nombre=nombre.split(' ')
if len(nombre)==4:
    lista_auxiliar=nombre[:2]
    nueva_lista=nombre[2:]+lista_auxiliar
elif len(nombre)==3:
    lista_auxiliar=[nombre[2]]
    nueva_lista=lista_auxiliar+nombre[:2]
elif len(nombre)==2:
    nueva_lista=nombre
    nueva_lista.reverse()
for i in range(len(nueva_lista)):
    print(nueva_lista[i][0].upper()+'.', end=" ")
