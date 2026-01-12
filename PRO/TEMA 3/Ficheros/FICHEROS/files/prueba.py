# fichero = open('ficheros/fichero01.txt', 'r')
# fichero.close()

try:
    fichero = open('files/fichero01.txt', 'r')
    textoaux = fichero.readlines()
    texto = []
    
    for linea in textoaux:
        texto.append(linea[:-1])

except:
    print("Ha ocurrido un error con el fichero\n")
else:
    for linea in texto:
        print(linea)
    print("Fin de ejecución...")
    

