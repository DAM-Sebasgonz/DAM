try:
    fichero = open('dir_trab/fichero02.txt', 'r')
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    caracter = fichero.read(1)
    while caracter != "":
        print(caracter, end ='')
        caracter = fichero.read(1)
    print()
    fichero.close()