'''Realizar un programa que mediante un diccionario asocie a cada letra el nº de veces que aparece en una frase como 
la primera letra de una palabra'''

frase = input("Introduce una frase: ").lower()
diccionario={}

#Crearía una lista con 
#limpiar frase
frase = frase.replace(".", "")
frase = frase.replace(",", "")
frase = frase.replace(":", "")
frase = frase.replace("¿", "")
frase = frase.replace("?", "")
frase = frase.replace(":", "")
frase = frase.replace("¡", "")
frase = frase.replace(";", "")
lista=frase.split()

print(lista)
for palabras in lista:
    diccionario.setdefault(palabras[0], 0)
    diccionario[palabras[0]] +=1

for clave in sorted(diccionario):
    print(f'La letra {clave} aparece {diccionario[clave]} veces en la frase.')
