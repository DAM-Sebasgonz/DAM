# se leen líneas del teclado y se escriben a un fichero

try:
    fichero = open('dir_trab/pruebaescritura.txt', 'w')
except:
    print("Ha ocurrido un error con el fichero\n")
else:
    while True:
        # tener cuidado que al leer de teclado el \n no se almacena
        texto = input('Línea de texto ->: ')
        if texto == '':              # para terminar el bucle
            break
        fichero.write(texto + '\n')  # hay que forzar el \n en la escritura
    fichero.close()