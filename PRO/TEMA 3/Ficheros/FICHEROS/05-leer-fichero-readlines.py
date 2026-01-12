# uso de readlines para la lectura de un fichero

try:
    fichero = open('dir_trab/fichero011.txt', 'r')
    textoaux = fichero.readlines()
    for linea in textoaux[:-1]:     # todas menos la última línea 
        print(linea[:-1])           # para eliminar el '\n leído
    print('***')
    print(textoaux[-1])             # última línea separada porque no tiene \n
    fichero.close()
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    print("Fin de ejecución...")

# lista = [1,2,3]

# for numero in lista[:-1]:
#     print(numero)