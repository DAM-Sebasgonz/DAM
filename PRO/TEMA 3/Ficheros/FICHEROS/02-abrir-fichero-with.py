# uso de with para el trabajo con ficheros
# al salir de la sentencia with el fichero es cerrado

with open('ficheros/fichero01.txt', 'r') as fichero:
    print(f'El fichero ha sido abierto en modo: {fichero.mode}')
