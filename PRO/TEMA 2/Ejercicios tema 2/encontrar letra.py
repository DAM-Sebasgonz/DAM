# Ejercicio 02
# Escriba un programa en Python que mediante un diccionario cuente el número de
# veces que aparece una letra en una frase leída.
# Una vez creado el diccionario se debe recorrer para mostrar por línea el número de
# ocurrencia de cada letra. 

# dicc_letras ={}

# letra = input("letra -->")

# if letra in dicc_letras:
#     print(f"la letra {letra} esta en el diccionario")
# else:
#     print(f"La letra {letra} NO esta en el diccionario")

# if dicc_letras.get(letra) == None:
#     print(f"La letra {letra} NO esta en el diccionario")
# else:
#     print(f"La letra{letra} esta en el diccionario")

frase = input("Ingrese una frase: ")

contador = {}

for letra in frase:
    letra = letra.lower()
    
    if letra.isalpha():
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

print("\nConteo de letras:")
print("-" * 30)

for letra, cantidad in contador.items():
    print(f"La letra '{letra}' aparece {cantidad} veces")

print("-" * 30)
print(f"Total de letras: {sum(contador.values())}")

