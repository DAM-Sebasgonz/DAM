'''Dado un diccionario de entrada, escriba un programa que lo ordene en base a sus valores de forma ascendente'''

'''Se puede asumir que:
*Tanto las claves como los valores del diccionario de entrada van a ser cadenas de texto. '''
'''*Tanto las claves como los valores del diccionario de entrada no van a contender dos puntos ':' '''
'''La salida tiene que ser una lista de tuplas (clave, valor) ya ordenadas.'''
diccionario1 ={}
while True:
    clave1=input("Dime una clave para diccionario 1: ")
    valor1=input("Dime un valor para la clave del diccionario 1: ")
    salir=input("Escribe @para salir: ")
    if salir=='@':
        break
    else:
        diccionario1[clave1]=valor1

# Ordenamos el diccionario en base a los valores

diccionario1=diccionario1.items()
diccionario1=list(diccionario1)
print(diccionario1)
#ORDENAMIENTO POR FUERZA BRUTA - Sort no vale porque Python no sabe los criterios de ordenamiento de una tupla | en orden creciente.

for i in range(len(diccionario1)-1):
    for j in range(i+1, len(diccionario1)):
        if diccionario1[j][1]<diccionario1[i][1]:
            diccionario1[j], diccionario1[i] = diccionario1[i], diccionario1[j]

print(diccionario1)