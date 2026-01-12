# uso de readline para la lectura de un fichero
# el programa lee línea a línea el fichero y 
# lo muestra por pantalla

try:
    fichero = open('dir_trab/fichero01.txt', 'r')
    linea = fichero.readline()
    while linea != "":
        print(linea)
        linea = fichero.readline() 
    fichero.close()
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    print("Fin de ejecución...")