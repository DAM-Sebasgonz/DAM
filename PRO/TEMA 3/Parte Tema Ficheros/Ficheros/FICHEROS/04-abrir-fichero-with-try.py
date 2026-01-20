try:
    # aquí se abre y realizan las operaciones con el fichero
    with open('ficheros/fichero01.txt', 'r') as fichero:
        print(f'El fichero ha sido abierto en modo: {fichero.mode}')
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    # aquí no se pueden realizar operaciones con el fichero 
    # fue cerrado al salir del with
    pass


