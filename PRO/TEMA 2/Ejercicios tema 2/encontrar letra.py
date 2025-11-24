# Ejercicio 02
# Escriba un programa en Python que mediante un diccionario cuente el número de
# veces que aparece una letra en una frase leída.
# Una vez creado el diccionario se debe recorrer para mostrar por línea el número de
# ocurrencia de cada letra. 

dicc_letras ={}

letra = input("letra -->")

if letra in dicc_letras:
    print(f"la letra {letra} esta en el diccionario")
else:
    print(f"La letra {letra} NO esta en el diccionario")

if dicc_letras.get(letra) == None:
    print(f"La letra {letra} NO esta en el diccionario")
else:
    print(f"La letra{letra} esta en el diccionario")

