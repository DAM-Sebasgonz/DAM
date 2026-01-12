try:
    fichero = open('dir_trab/fichero01.txt', 'r')
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    texto = fichero.read()
    print(texto)    
    fichero.close()