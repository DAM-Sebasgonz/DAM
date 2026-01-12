import csv
lista = []

# versión usando with

with open ("files/DatosPersonas.csv", "r", newline="\n") as csvfile:

    # creamos un objeto con el método reader() para la lectura de los datos
    reader = csv.reader(csvfile, delimiter = ";")  
 
    # en el objeto reader se irán guardando todos los datos 

    # IMPORTANTE -- los datos del reader sólo se puede recorrer una única vez

    for nombre, empleo, email in reader:
        # imprimir en pantalla
        print (nombre, empleo, email)

    # for tupla in reader:
    #     # imprimir en pantalla la tupla que se ha obtenido
    #     print (tupla)

    # lo almacenamos en una lista para posteriormente trabajar con ella

    # for nombre, empleo, email in reader: 
    #     # generar de nuevo la lista original
    #     lista.append((nombre, empleo, email))

#     for tupla in reader: 
#         # generar de nuevo la lista original
#         lista.append(tupla)

# for elemento in lista:
#     print(elemento)

# versión 02 sin usar with

# import csv
# lista = []

# csvfile = open ("files/DatosPersonas.csv", "r", newline="\n")
# reader = csv.reader(csvfile, delimiter = ";")

#     # en reader está todo lo leído cada elemento es una tupla
#     # que corresponde a una los elementos de una fila del fichero
    
# for nombre, empleo, email in reader:
#     # imprimir en pantalla
#     print (nombre, empleo, email)

# # cerramos el fichero despúes de usados los datos de la lista generada por el reader

# csvfile.close() 

# # IMPORTANTE -- la lista de datos sólo se puede recorrer una única vez

# # for tupla in reader:
# #     # imprimir en pantalla la tupla que se ha obtenido
# #     print (tupla)
# # csvfile.close() 

# # o lo almacenamos en una lista para posteriormente trabajar con ella

# # for nombre, empleo, email in reader: 
# #     # generar de nuevo la lista original
# #     lista.append((nombre, empleo, email))
# # csvfile.close() 

# # for tupla in reader: 
# #     # generar de nuevo la lista original
# #     lista.append(tupla)
# # csvfile.close() 

# # for elemento in lista:
# #     print(elemento)