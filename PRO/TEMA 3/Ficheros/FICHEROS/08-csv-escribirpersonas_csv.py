# método 01

# para imprimir un fichero en formato csv sin encabezado
# se necesita que los datos estén en una lista
#
# cada elemento de esa lista debe ser una tupla/lista
# en la que están los campos de datos que se quieren escribir


import csv

# lista = [['11111111', 'Reinaldo González', 'Profesor'],\
#     ('22222222', 'Juan María Hernández', 'Paro'),\
#         ('33333333', 'Rosario García Expósito', 'Comerciante'),\
#             ('44444444', 'María Pérez García', 'Médica')]           # esta es la lista con 4 tuplas/listas

# with open("files/DatosPersonasCopia.csv","w") as f:   # abrimos ficnero escritura
#     writer = csv.writer(f, delimiter=";")                           # creamos el objeto writer indicando delimitador

#     for fila in lista:                                              # recorremos la lista
#         writer.writerow(fila)                                       # escribimos en el fichero una línea
                                                                    # con los campos de la tupla separados por el delimitador
                            
# para verificar el fichero creado haga 
# % type files/DatosPersonasCopia.csv


# método 02

# para imprimir un fichero en formato csv CON encabezado
# primero se necesita en una lista los nombres de los campos
#
# luego de abierto el fichero se escribe el encabezado
# para cada línea que se quiera escribir en el fichero
# se debe crear un diccionario
# donde la clave son los nombres de los campos y los valores 
# los valores que deben aparecer en el fichero.

lista_campos = ['dni', 'nombre_apellidos', 'profesión_actual']      # la lista de los campos

lista_datos = [['11111111', 'Reinaldo González', 'Profesor'],\
    ('22222222', 'Juan María Hernández', 'Paro'),\
        ('33333333', 'Rosario García Expósito', 'Comerciante'),\
            ('44444444', 'María Pérez García', 'Médica')]           # esta es la lista con 4 tuplas/listas
                                                                    # cada una de ellas será una línea del fichero

with open("files/DatosPersonasEncabezadoCopia.csv","w", newline="\n") as f:   # abrimos ficnero escritura
    writer = csv.DictWriter(f, fieldnames=lista_campos)                       # creamos el objeto writer indicando los campos a usar

    writer.writeheader()                                        # escribimos encabezado en el fichero
    for datos in lista_datos:   # 3 variables una por cada campo  
        dicc_aux = {lista_campos[0]:datos[0],\
                    lista_campos[1]:datos[1],\
                        lista_campos[2]:datos[2]}         # creamos el diccionario

        writer.writerow(dicc_aux)                               # lo escribimos como una línea del fichero