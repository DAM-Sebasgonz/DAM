try:
    fichero = open('', 'r')
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    texto = fichero.read()
    print(texto)    
    fichero.close()