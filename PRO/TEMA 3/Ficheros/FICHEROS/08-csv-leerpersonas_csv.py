import csv

# método 1 fichero sin encabezado usando una lista

# lista = []                                          # para almacemar las filas
# with open("files/DatosPersonas.csv","r", newline="\n") as f:
#     reader = csv.reader(f, delimiter=";")
#     for fila in reader:
#         print(fila)                                 # cada fila(línea) es una lista
#         lista.append(fila)                          # añadimos a la lista la fila 
# print()
# print(lista)                                        # imprimimos la lista de las líneas 

# método 2 fichero CON ENCABEZADO usando un diccionario

lista = []                                        # para almacenar las filas

dict = {}
with open("files/DatosPersonasEncabezado.csv", "r", newline= "\n") as f:
    reader = csv.DictReader(f, delimiter=";")
    for fila in reader:
        print(fila)                               # cada fila(linea) es un diccionario
        lista.append(fila)                        # añadimos el diccionario a la lista
print()                                                 
print(lista)                                      # imprimimos la lista de las líneas