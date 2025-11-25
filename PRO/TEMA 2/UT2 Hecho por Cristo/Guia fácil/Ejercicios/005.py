'''
Escriba un programa en Python que indique si todos los elementos de una lista son iguales. La 
lista debe mostrar la lista e indicar si todos sus elementos son iguales. '''
# lista=[]
# es_verdad=True
# while True:
#     entrada=input("Introduce una entrada hasta que quieras salir (@): ").lower()
#     if entrada=='@':
#         break
#     else:
#         if entrada.isdigit():
#             lista.append(int(entrada))
#             continue
#         else:
#             lista.append(entrada)
# for elto in range(1, len(lista)):
#     if type(lista[elto])!=type(lista[0]):
#         es_verdad=False
#         break
# if es_verdad==False:
#     print("La lista no tiene todos los elementos iguales.")
# else:
#     print("La lista tiene todos los elementos iguales.")
#     print("La lista es:", lista)
#otra versión
lista=[]
es_verdad=True
while True:
    entrada=input("Introduce una entrada hasta que quieras salir (@): ").lower()
    if entrada=='@':
        break
    else:
        if entrada.isdigit():
            lista.append(int(entrada))
            continue
        else:
            lista.append(entrada)
for elto in lista:
    if elto!=lista[0]:
        es_verdad=False
        break
if es_verdad==False:
    print("La lista no tiene todos los elementos iguales.")
else:
    print("La lista tiene todos los elementos iguales.")
    print("La lista es:", lista)