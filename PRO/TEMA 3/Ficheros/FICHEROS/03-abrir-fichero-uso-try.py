try:
    fichero = open('ficheros/fichero01.txt', 'r')
    #codigo
except:
    print("Ha ocurrido un error con el fichero")
else:
    # aquí se pueden realizar las operaciones con el fichero
    #codigo
    print(f'El fichero ha sido abierto en modo: {fichero.mode}')
    fichero.close()