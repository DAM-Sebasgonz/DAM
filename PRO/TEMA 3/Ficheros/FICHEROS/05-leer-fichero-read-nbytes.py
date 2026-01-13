# muestra contenido de un fichero por pantalla
try:
    fichero = open('ficheros/fichero01.txt', 'r')
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    caracter = fichero.read(1)
    while caracter != "":
        print(caracter)
        caracter = fichero.read(1)
    fichero.close()