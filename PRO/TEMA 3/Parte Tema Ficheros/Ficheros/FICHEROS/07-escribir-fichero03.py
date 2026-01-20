# usando writelines()

# lista = ['línea 01','línea 03', 'línea 03']
lista = ['línea 01\n','línea 02\n', 'línea 03']

try:
    fichero_escritura = open('dir_trab/fichero03.txt', 'w')
except:
    print("Ha ocurrido un error con el fichero de escritura\n")
else:
    # aquí se pueden realizar las operaciones con el fichero

    fichero_escritura.writelines(lista)
    fichero_escritura.close()


# otra alternativa de uso de writelines

# try:
#     # fichero = open('dir_trab/pruebaescritura.txt', 'w')
#     fichero = open('dir_trab/pruebaescritura.txt', 'a')
# except:
#     print("Ha ocurrido un error con el fichero\n")
# else:
#     # aquí se pueden realizar las operaciones con el fichero
#     lista = ['línea03', 'línea04', 'línea05']
#     for linea in lista:
        
#         # otra alternativa writelines
#         # lo que se vaya a escribir en una lista
#         # tener cuidado que writeline tampoco escribe \n
        
#         fichero.writelines(linea+'\n') 
#     fichero.close()