'''Escribir un programa en Python para eliminar claves con los mismos valores en un
diccionario.
Ejemplo:
d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
La solución es {'three': 3, 'four': 44}'''
diccionario={}
try:
    registros=int(input("Escribe una cantidad de registros para el diccionario >0: "))
except:
    print("Error. Escribe una clave válida.")
else:
    for i in range(registros):
        clave=input("Ingresa una clave: ")
        valor=input("Ingresa un valor: ")
        diccionario[clave]=valor
print(diccionario)
print(iterador:= diccionario.values()) # operador walrus
#recorrer el diccionario en busca de elementos coincidentes
valores_vistos = []
valores_repetidos = []
# Determinar los valores únicos y repetidos

for valor in diccionario.values():
    if valor in valores_vistos and valor not in valores_repetidos:
        valores_repetidos.append(valor)
    elif valor not in valores_vistos:
        valores_vistos.append(valor)
'''Ahora queremos crear un nuevo diccionario sin los valores repetidos. Para eso:
Revisamos cada clave y valor del diccionario original.
Si el valor no está en valores_repetidos, lo copiamos al nuevo diccionario diccionario_filtrado.'''
diccionario_filtrado={}
for clave, valor in diccionario.items():
    if valor not in valores_repetidos:
        diccionario_filtrado[clave]=valor
print(diccionario_filtrado)
