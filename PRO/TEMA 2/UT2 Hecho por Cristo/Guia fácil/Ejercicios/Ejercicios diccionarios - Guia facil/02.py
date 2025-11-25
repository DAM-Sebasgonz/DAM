'''Escribe un programa en Python que mediante un diccionario cuente el nº de veces que aparece una letra en una frase leída.

# Una vez creado el diccionario se debe recorrer para mostrar por línea el nº de ocurrencia de cada letra.'''

# frase = input("Introduce una frase: ")

# diccionario = {}

# for letra in frase.lower():
#     if letra.isalpha():
#         if letra in diccionario:
#             diccionario[letra] += 1
#         else:
#             diccionario[letra] = 1

# for letra, ocurrencias in diccionario.items():
#     print(f"{letra}: {ocurrencias} ", end=" ")

'''Nuevo ejercicio'''
#versión 2: UTILIZANDO .SETDEFAULT()
frase = input("Introduce una frase: ")

diccionario = {}

for letra in frase.lower():
    if letra.isalpha():
        if letra not in diccionario:    
            diccionario.setdefault(letra, 1)
        else:
            diccionario[letra] += 1

for letra in diccionario:
    print(f"{letra}: = {diccionario[letra]} ", end=" ")